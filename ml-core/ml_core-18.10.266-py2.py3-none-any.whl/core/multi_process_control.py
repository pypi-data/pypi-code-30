# -*- coding: utf8 -*-
import copy
import logging
import multiprocessing
import threading
import uuid
from multiprocessing import Pool
import os
import signal


DEFAULT_USE_THREADS = True


def process_worker_init(parent_id):
    def sig_int(_signal_num, _frame):
        os.kill(parent_id, signal.SIGSTOP)

    def sig_int_sef_fault(_signal_num, _frame):
        os.kill(parent_id, signal.SIGTERM)

    signal.signal(signal.SIGINT, sig_int)
    signal.signal(signal.SIGSEGV, sig_int_sef_fault)


class _MultiProcessControlShim(object):
    def __init__(self, use_threads=None):
        if use_threads is None:
            self.__use_threads = DEFAULT_USE_THREADS
        else:
            self.__use_threads = use_threads

    class MultiShimFuture(object):
        def wait(self):
            pass

    @classmethod
    def execute(cls, method, args, callback=None, high=False):
        method(*args)
        if callback is not None:
            callback(None)

        return cls.MultiShimFuture()

    @property
    def using_threads(self):
        return self.__use_threads

    def terminate(self):
        pass

    def close(self):
        pass

    def join(self):
        pass


def get_multi_process_control(processes, use_threads=None):
    if processes == 1:
        return _MultiProcessControlShim(use_threads=use_threads)

    if use_threads is None:
        use_threads = DEFAULT_USE_THREADS

    if use_threads is True:
        use_processes = os.environ.get('MALI_PROCESSES', '0') == '1'
        use_threads = not use_processes

    return _MultiProcessControl(processes, use_threads)


class _MultiProcessControl(object):
    def __init__(self, processes, use_threads):
        processes = multiprocessing.cpu_count() * 5 if processes == -1 else processes
        self.__using_threads = False
        self.__controllers = multiprocessing.Semaphore(processes)
        self.__pending_jobs = []
        self.__processing_pool_high = None

        if use_threads:
            self.__use_threads(processes)
        else:
            try:
                self.__processing_pool = Pool(processes, process_worker_init, initargs=(os.getpid(),))
            except AssertionError:
                self.__use_threads(processes)

        self._jobs_lock = threading.Lock()
        self._jobs = {}

    @property
    def using_threads(self):
        return self.__using_threads

    def __use_threads(self, processes):
        from multiprocessing.pool import ThreadPool

        self.__using_threads = True
        self.__processing_pool = ThreadPool(processes)
        self.__processing_pool_high = ThreadPool(1)

    def join(self):
        logging.debug('%s pool joining', self.__class__)
        self.__wait_pending_jobs()
        logging.debug('%s pool joined', self.__class__)

    def close(self):
        if self.__processing_pool is not None:
            logging.debug('%s closing & joining pool', self.__class__)
            self.__processing_pool.close()
            self.join()

    def __wait_pending_jobs(self):
        while True:
            with self._jobs_lock:
                jobs = copy.copy(self._jobs)

            if len(jobs) == 0:
                break

            for token, async_result in jobs.items():
                if async_result is not None:
                    async_result.wait()

            self.__check_pending_jobs()

    def __check_pending_jobs(self):
        updates_jobs = False

        with self._jobs_lock:
            jobs = copy.copy(self._jobs)

        for token, async_result in jobs.items():
            if async_result is None or not async_result.ready():
                continue

            async_result.get()

            jobs[token] = None
            updates_jobs = True

        if updates_jobs:
            with self._jobs_lock:
                self._jobs = {token: async_result for token, async_result in jobs.items() if async_result is not None}

    def execute(self, method, args, callback=None, high=False):
        self.__check_pending_jobs()

        token = uuid.uuid4()
        processing_pool = self.__processing_pool_high if high and self.__processing_pool_high else self.__processing_pool

        job_async_result = processing_pool.apply_async(
            method,
            args=args,
            callback=callback)

        with self._jobs_lock:
            self._jobs[token] = job_async_result

        return job_async_result

    def terminate(self):
        self.__processing_pool.terminate()
        with self._jobs_lock:
            self._jobs = {}
