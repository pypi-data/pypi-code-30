import asyncio
import logging
import string

import docker

from ..cloud_logger import CloudLogger
from ..invocation_docker import InvocationDocker

logger = logging.getLogger(__name__)
printable_set = frozenset(string.printable + '\n')


class DockerExecution(object):
    async def on_log(self, x, step_name=None):
        filtered_string = CloudLogger.get_printable(x)
        if filtered_string:
            x = f"{filtered_string}"
            logger.debug(x)
        return x

    async def on_stats(self, x):

        await self.send_full_command('JOB_STATS', 1, **x)
        await self.sleep(10)

    @classmethod
    def create(cls, send, **kwargs):
        return cls(send, **kwargs)

    async def log(self, line, step_name=None):
        step_name = step_name or 'CloudLogger'
        await asyncio.wait([log_handler(line, step_name=step_name) for log_handler in (self.log_handlers or [])])

    def __init__(self, send, active_config=None, **kwargs):
        from .api_commands import send_command

        self.send = send
        self.active_config = active_config
        self.invocation_id = kwargs['invocation_id']
        self.logging_endpoint = kwargs.pop('logging_endpoint', None)
        self.log_handlers = [self.on_log]
        self.remote_logger = None
        if self.logging_endpoint is not None:
            logger.debug('%s will remote log to %s', self.invocation_id, self.logging_endpoint)
            self.remote_logger = CloudLogger(self.logging_endpoint)
            self.log_handlers.append(self.remote_logger.on_log)
        self.invocation = {}
        self.invocation.update(kwargs)
        self.container = InvocationDocker.create(**kwargs, active_config=self.active_config, log_callback=self.log, stats_call_back=self.on_stats)
        # hosted here for mocking
        self.sleep = asyncio.sleep
        self.send_command = send_command

    async def send_full_command(self, command_name, command_version, **kwargs):
        kwargs['invocation_id'] = self.invocation_id
        logger.debug('send_full_command(%s, %s, %s)', command_name, command_version, kwargs)
        return await self.send_command(self.send, command_name, command_version, **kwargs)

    async def run_manged(self):
        exit_code = None
        await self.send_full_command('JOB_START', 1, **self.invocation)
        try:
            exit_code = await self.container.do_run()
        except docker.errors.APIError as ex:
            logger.exception(ex)
            exit_code = ex.explanation

        finally:
            from .api_commands import send_command
            await self.send_full_command('JOB_END', 1, exit_code=exit_code)
            if self.remote_logger:
                await self.remote_logger.close()
