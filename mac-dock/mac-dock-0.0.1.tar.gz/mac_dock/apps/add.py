#!/usr/bin/env python
import click
import mac_dock

PROG_NAME = 'python -m %s' % "mac_dock.apps.add"


@click.command()
@click.argument('path', nargs=-1)
def _cli(path):
    mac_dock.apps.add(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
