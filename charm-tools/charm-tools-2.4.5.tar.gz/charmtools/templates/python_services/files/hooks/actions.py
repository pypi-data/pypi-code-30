from charmhelpers.core import hookenv


def log_start(service_name):
    hookenv.log('$metadata.package starting')
