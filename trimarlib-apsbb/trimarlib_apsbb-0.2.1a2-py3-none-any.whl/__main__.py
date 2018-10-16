import argparse
import logging
import signal
import threading

from .logging import setup_logging
from .server import Server
from .version import VERSION

CANCEL = threading.Event()


def sig_handler(signum, frame):
    logging.info('signal handler called: %s', signum)
    CANCEL.set()


signal.signal(signal.SIGTERM, sig_handler)

parser = argparse.ArgumentParser(
    prog='apsbblib',
    description='Run APSBackBone IPC server')
parser.add_argument(
    '-p', '--port',
    type=str,
    default='/dev/ttyS1',
    help='''\
serial port to be used as communication channel with the backbone hardware''')
parser.add_argument(
    '-b', '--baudrate',
    type=int,
    default=115200,
    help='''\
baudrate of the serial port towards the backbone hardware''')
parser.add_argument(
    '-v', '--verbose',
    action='count',
    help='''\
increase program verbosity''')
parser.add_argument(
    '--firmware',
    type=str,
    help='''\
path to the firmware to be verified and uploaded to the backbone hardware''')
parser.add_argument(
    '-V', '--version',
    action='version',
    version=VERSION)
ns = parser.parse_args()

if ns.verbose is None:
    setup_logging(level=logging.WARNING)
elif ns.verbose == 1:
    setup_logging(level=logging.INFO)
else:
    setup_logging(level=logging.DEBUG)

try:
    with Server(port=ns.port, baudrate=ns.baudrate):
        logging.info('APSBackBone IPC server running, version=%s.', VERSION)
        CANCEL.wait()
        logging.info('cancellation requested')
except KeyboardInterrupt:
    logging.info('interrupted')
except RuntimeError:
    logging.exception('failed to start server')
    exit(1)
