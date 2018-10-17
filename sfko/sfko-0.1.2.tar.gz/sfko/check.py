import math
import time
from pprint import pprint

from .constant import BackendType
from .register import register_check
from .util.log import Log
from .util.proxy import AWS_REGEX, GCP_REGEX
from .util.redis import (count_pending_replication, get_pending_replication,
                         get_requests)

_log = Log('check')

# Convenience function for dealing with Request objects

def has_status(requests, code = 200):
    '''
    Takes a list of Requests, and optionally a status code
    Returns a bool indicating if any of them have status == code
    '''
    for req in requests:
        print(req)
        if req.status == code:
            return True
    return False

def _check_backend_key(bucket, key, cloud):
    delete_key, requests = get_requests(bucket, key, cloud)
    passed = True
    if not requests:
        passed = False
    else:
        has_200 = False
        for req in requests:
            if req.status == 200:
                has_200 = True
        if not has_200:
            passed = False
    if not passed:
        _log.error('%s/%s failed to be uploaded to the backend!'%(bucket, key))
    delete_key()
    return passed

@register_check('check-backend')
def check_backend(bucket_conf, objs):
    passed = True
    for bucket, key in objs.objects:
        if not _check_backend_key(bucket, key, bucket_conf.backend.type.friendly()):
            passed = False
    return passed



def _check_aws_mpu(bucket, key, cloud):
    _log.debug('Checking AWS MPU %s:%s:%s'%(bucket, key, cloud))
    passed = True
    delete_key, requests = get_requests(bucket, key, cloud)
    if not requests:
        passed = False
    inits = [x for x in requests if x.tag == 'mpu_init']
    parts = [x for x in requests if x.tag == 'mpu_part']
    comps = [x for x in requests if x.tag == 'mpu_comp']
    if not inits or not parts or not comps:
        _log.error('%s/%s failed to be uploaded to the backend!'%(bucket, key))
        passed = False
    if not has_status(inits) or not has_status(comps):
        passed = False
    succeeded_parts = sorted([x.extra['part'] for x in parts if x.status == 200])
    if len(succeeded_parts) != succeeded_parts[-1]:
        passed = False
    delete_key()
    return passed

def _check_gcp_mpu(bucket, key, cloud):
    _log.debug('Checking GCP MPU %s:%s:%s'%(bucket, key, cloud))
    passed = True
    delete_key, requests = get_requests(bucket, key, cloud)
    if not requests:
        passed = False
    inits = [x for x in requests if x.tag == 'mpu_init']
    parts = [x for x in requests if x.tag == 'mpu_part']
    copys = [x for x in requests if x.tag == 'mpu_copy']
    comps = [x for x in requests if x.tag == 'mpu_comp']
    if not inits or not parts or not copys or not comps:
        _log.error('%s/%s failed to be uploaded to the backend!'%(bucket, key))
        passed = False
    if not has_status(inits) or not has_status(comps):
        passed = False
    succeeded_parts = sorted([x.extra['part'] for x in parts if x.status == 200])
    if len(succeeded_parts) != succeeded_parts[-1]:
        passed = False
    needed_copies = math.ceil(len(succeeded_parts) / 32)
    if needed_copies > 1:
        needed_copies += 1 # Add one for the final stage
    succeeded_copies = len([x.extra['part'] for x in copys if x.status == 200])
    if needed_copies != succeeded_copies:
        passed = False
    return passed

@register_check('check-mpu')
def check_mpu(bucket_conf, objs):
    if bucket_conf.backend.type is BackendType.AWS:
        for bucket, key in objs.objects:
            if not _check_aws_mpu(bucket, key, bucket_conf.backend.type.friendly()):
                return False
    elif bucket_conf.backend.type is BackendType.GCP:
        for bucket, key in objs.objects:
            if not _check_gcp_mpu(bucket, key, bucket_conf.backend.type.friendly()):
                return False
    return True


def _wait_for_replication(bucket_conf, objs):
    time.sleep(10)
    expiry = 600 + time.time() # 10 Minutes from now
    while expiry > time.time():
        if count_pending_replication(bucket_conf.backend.type.friendly()) > 0:
            time.sleep(5)
        else:
            _log.debug('Replication complete')
            return True
    _log.error('Some objects failed to replicate before the timeout elapsed!')
    _log.debug(get_pending_replication(bucket_conf.backend.type.friendly()))
    return False


@register_check('check-replication')
def check_replication(bucket_conf, objs):
    if _wait_for_replication(bucket_conf, objs):
        for bucket, key in objs.objects:
            if not _check_backend_key(bucket, key, bucket_conf.replication.type.friendly()):
                return False
        return True
    return False


@register_check('check-replication-mpu')
def check_replication_mpu(bucket_conf, objs):
    if _wait_for_replication(bucket_conf, objs):
        if bucket_conf.replication.type is BackendType.AWS:
            for bucket, key in objs.objects:
                if not _check_aws_mpu(bucket, key, bucket_conf.replication.type.friendly()):
                    return False
            return True
        elif bucket_conf.replication.type is BackendType.GCP:
            for bucket, key in objs.objects:
                if not _check_gcp_mpu(bucket, key, bucket_conf.replication.type.friendly()):
                    return False
            return True
    return False
