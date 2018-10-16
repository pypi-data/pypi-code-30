#!/usr/bin/env python
import click
import mac_dock

PROG_NAME = 'python -m %s' % "mac_dock.folders.add"


@click.command()
@click.argument('path', required=True)
@click.option('--arrangement', help='sort by: 1 - name (default), 2 - added, 3 - modification, 4 - creation, 5 - kind')
@click.option('--displayas', help='display as: 1 - folder, 2 - stack (default)')
@click.option('--showas', help='show as: 1 - beep, 2 - grid, 3 - list, 4 - auto (default)')
def _cli(path, arrangement=None, displayas=None, showas=None):
    mac_dock.folders.add(path, arrangement=arrangement, displayas=displayas, showas=showas)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
