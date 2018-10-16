"""Command line interface."""

# Copyright 2016-2018 ASI Data Science
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import division

import contextlib
import os
import os.path
import shutil
import stat
import subprocess
import sys
import tempfile
import textwrap
import time
import uuid
from distutils.version import StrictVersion

import click
import requests
import sml.auth
import sml.config
import sml.baskerville
import sml.casebook
import sml.client
import sml.galleon
import sml.hound
import sml.shell
import sml.update
import sml.version
from tabulate import tabulate

CREDENTIALS_FILE = sml.config._credentials_file_path("sherlockml")

SSH_OPTIONS = [
    "-o",
    "IdentitiesOnly=yes",
    "-o",
    "StrictHostKeyChecking=no",
    "-o",
    "BatchMode=yes",
]


class AmbiguousNameError(Exception):
    """Exception when name matches multiple servers."""

    pass


def _print_and_exit(msg, code):
    """Print error message and exit with given code."""
    click.echo(msg, err=True)
    sys.exit(code)


def _get_pypi_versions():
    """List releases available from PyPI."""
    response = requests.get("https://pypi.python.org/pypi/sml/json", timeout=1)
    versions = response.json()["releases"].keys()
    return [StrictVersion(v) for v in versions]


def _populate_creds_file():
    """Prompt user for client ID and secret and save them."""
    while True:
        domain = click.prompt(
            "Domain", default="services.sherlockml.com", err=True
        )
        client_id = click.prompt("Client ID", err=True).strip()
        client_secret = click.prompt("Client secret", err=True).strip()

        if sml.auth.credentials_valid(
            client_id, client_secret, domain, "https"
        ):
            break
        click.echo("Invalid credentials. Please try again.", err=True)

    credentials = textwrap.dedent(
        """\
    [default]
    client_id = {client_id}
    client_secret = {client_secret}
    domain = {domain}
    """.format(
            client_id=client_id, client_secret=client_secret, domain=domain
        )
    )
    try:
        os.makedirs(os.path.dirname(CREDENTIALS_FILE))
    except OSError:
        pass
    with open(CREDENTIALS_FILE, "w") as creds_file:
        creds_file.write(credentials)
    os.chmod(
        CREDENTIALS_FILE,
        stat.S_IRUSR | stat.S_IWUSR & ~stat.S_IRGRP & ~stat.S_IROTH,
    )


def _check_creds_file_perms():
    """Check the permissions of the credentials file are correct."""
    if oct(os.stat(CREDENTIALS_FILE).st_mode & 0o777)[-2:] != "00":
        msg = textwrap.dedent(
            """\
        Permissions for {0} are too open.
        Your credentials file must not be accessible to other users on this
        computer.
        Run 'chmod 0600 {0}' to fix this.""".format(
                CREDENTIALS_FILE
            )
        )
        _print_and_exit(msg, 66)


def _ensure_creds_file_present():
    """Ensure the user's credentials file is present."""
    try:
        open(CREDENTIALS_FILE)
    except IOError:
        msg = textwrap.dedent(
            """\
        It looks like this is the first time you've used sml on this computer,
        so you must enter your SherlockML credentials. They'll be saved so you
        don't have to enter them again.
        """
        )
        click.echo(msg, err=True)
        _populate_creds_file()


def _check_credentials():
    """Check if credentials are present in environment or config file."""
    try:
        sml.config.get_credentials()
    except sml.config.CredentialsError:
        _ensure_creds_file_present()
        _check_creds_file_perms()


def _resolve_project(project):
    """Resolve a project name or ID to a project ID."""
    try:
        project_id = uuid.UUID(project)
    except ValueError:
        user_id = sml.auth.user_id()
        client = sml.casebook.Casebook()
        project_id = client.get_project_by_name(user_id, project).id_
    return project_id


def _server_by_name(project_id, server_name, status=None):
    """Resolve a project ID and server name to a server ID."""
    client = sml.galleon.Galleon()
    matching_servers = client.get_servers(project_id, server_name, status)
    if len(matching_servers) == 1:
        return matching_servers[0]
    else:
        if not matching_servers:
            tpl = 'no {} server of name "{}" in this project'
        else:
            tpl = (
                'more than one {} server of name "{}", please select by '
                "server ID instead"
            )
        adjective = "available" if status is None else status
        raise AmbiguousNameError(tpl.format(adjective, server_name))


def _any_server(project_id, status=None):
    """Get any running server from project."""
    client = sml.galleon.Galleon()
    servers_ = client.get_servers(project_id, status=status)
    if not servers_:
        adjective = "available" if status is None else status
        _print_and_exit("No {} server in project.".format(adjective), 78)
    return servers_[0].id_


def _resolve_server(project, server=None, ensure_running=True):
    """Resolve project and server names to project and server IDs."""
    project_id = _resolve_project(project)
    status = "running" if ensure_running else None
    try:
        server_id = uuid.UUID(server)
    except ValueError:
        server_id = _server_by_name(project_id, server, status).id_
    except TypeError:
        server_id = _any_server(project_id, status)
    return project_id, server_id


def _environment_by_name(project_id, environment_name):
    client = sml.baskerville.Baskerville()
    matching_environments = client.get_environments(
        project_id, environment_name
    )
    if len(matching_environments) == 1:
        return matching_environments[0]
    else:
        if not matching_environments:
            tpl = 'no available environment of name "{}"'
        else:
            tpl = (
                'more than one environment of name "{}", please select by '
                "environment ID instead"
            )
        raise AmbiguousNameError(tpl.format(environment_name))


def _resolve_environment(project_id, environment):
    """Resolve environment to environment IDs."""
    try:
        environment_id = uuid.UUID(environment)
    except ValueError:
        environment_id = _environment_by_name(project_id, environment).id_
    return environment_id


@contextlib.contextmanager
def _save_key_to_file(key):
    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, "key.pem")
    with open(filename, "w") as keyfile:
        keyfile.write(key)
    os.chmod(filename, stat.S_IRUSR & ~stat.S_IRGRP & ~stat.S_IROTH)
    yield filename
    shutil.rmtree(tmpdir)


def _get_ssh_details(project_id, server_id):
    client = sml.galleon.Galleon()
    for _ in range(20):
        try:
            return client.ssh_details(project_id, server_id)
        except sml.auth.AuthenticationError as err:
            _print_and_exit(err, 77)
        except sml.client.SherlockMLServiceError:
            click.echo("Server still starting, waiting 30 seconds")
        time.sleep(30)
    _print_and_exit("Could not connect to server", 69)


PERMISSION_DENIED_MESSAGE = """
Permission was denied when attempting to connect to your SherlockML server. A
bug in earlier versions of OpenSSH (including the version distributed with
macOS 10.10) may be the cause - please try updating your operating system or
SSH version and try again.
""".replace(
    "\n", " "
).strip()


def _run_ssh_cmd(argv):
    """Run a command and print a message when a string is matched."""
    process = subprocess.Popen(argv, stderr=subprocess.PIPE)
    line = process.stderr.readline()
    while line:
        click.echo(line, nl=False, err=True)
        if b"Permission denied" in line:
            click.echo(PERMISSION_DENIED_MESSAGE, err=True)
        line = process.stderr.readline()
    return process.wait()


class SherlockMLCLIGroup(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            super(SherlockMLCLIGroup, self).__call__(*args, **kwargs)
        except AmbiguousNameError as err:
            _print_and_exit(err, 64)
        except sml.auth.AuthenticationError as err:
            _print_and_exit(err, 77)
        except sml.client.SherlockMLServiceError as err:
            _print_and_exit(err, 69)


@click.group(cls=SherlockMLCLIGroup)
def cli():
    """Command line interface to SherlockML."""
    try:
        sml.update.check_for_new_release()
    except Exception:  # pylint: disable=broad-except
        pass


@cli.command()
def version():
    """Print the sml version number."""
    click.echo(sml.version.__version__)


@cli.command()
def login():
    """Write SherlockML credentials to file."""
    if os.path.exists(CREDENTIALS_FILE):
        if not click.confirm("Overwrite existing credentials file?"):
            return
    _populate_creds_file()


@cli.command()
def home():
    """Open the SherlockML home page."""
    url = sml.config.frontend_url()
    click.launch("{}/home".format(url))


@cli.command()
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print extra information about projects.",
)
def projects(verbose):
    """List accessible SherlockML projects."""
    _check_credentials()
    client = sml.casebook.Casebook()
    user_id = sml.auth.user_id()
    projects_ = client.get_projects(user_id)
    if verbose:
        if not projects_:
            click.echo("No projects.")
        else:
            click.echo(
                tabulate(
                    [(p.name, p.id_) for p in projects_],
                    ("Project Name", "ID"),
                    tablefmt="plain",
                )
            )
    else:
        for project in projects_:
            click.echo(project.name)


@cli.group()
def server():
    """Manipulate SherlockML servers."""
    pass


@server.command(name="list")
@click.argument("project")
@click.option(
    "-a",
    "--all",
    is_flag=True,
    help="Show all servers, not just running ones.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print extra information about servers.",
)
def list_servers(project, all, verbose):
    """List your SherlockML servers."""
    _check_credentials()
    client = sml.galleon.Galleon()
    status_filter = None if all else "running"
    project_id = _resolve_project(project)
    servers_ = client.get_servers(project_id, status=status_filter)
    if verbose:
        if not servers_:
            click.echo("No servers.")
        else:
            headers = (
                "Server Name",
                "Type",
                "Machine Type",
                "CPUs",
                "RAM",
                "Status",
                "ID",
                "Started",
            )
            rows = []
            for server in servers_:
                if server.machine_type == "custom":
                    machine_type = "-"
                    cpus = "{:.3g}GB".format(server.milli_cpus / 1000)
                    memory_gb = "{:.3g}GB".format(server.memory_mb / 1000)
                else:
                    machine_type = server.machine_type
                    cpus = "-"
                    memory_gb = "-"
                rows.append(
                    (
                        server.name,
                        server.type_,
                        machine_type,
                        cpus,
                        memory_gb,
                        server.status,
                        server.id_,
                        server.created_at.strftime("%Y-%m-%d %H:%M"),
                    )
                )
            click.echo(tabulate(rows, headers, tablefmt="plain"))
    else:
        for server in servers_:
            click.echo(server.name)


@server.command(name="open")
@click.argument("project")
@click.option("--server", is_flag=False, help="Name or ID of server to use.")
def open_(project, server):
    """Open a SherlockML server in your browser."""
    project_id, server_id = _resolve_server(project, server)
    client = sml.galleon.Galleon()
    server = client.get_server(project_id, server_id)
    https_services = [
        service for service in server.services if service.name == "https"
    ]
    if not https_services:
        _print_and_exit(
            "Server {} is not running an application that "
            "can be opened in a web browser".format(server.name)
        )
    [https_service] = https_services
    url = "{}://{}".format(https_service.scheme, https_service.host)
    click.echo("Opening {}".format(url))
    click.launch(url)


@server.command()
@click.argument("project")
@click.option(
    "--cores",
    type=float,
    default=1,
    show_default=True,
    help="Number of CPU cores",
)
@click.option(
    "--memory",
    type=float,
    default=4,
    show_default=True,
    help="Server memory in GB",
)
@click.option(
    "--type",
    "type_",
    is_flag=False,
    default="jupyter",
    show_default=True,
    help="Server type",
)
@click.option(
    "--machine-type",
    "machine_type",
    default=None,
    show_default=False,
    help="Machine type for a dedicated instance, e.g. m5.xlarge. "
    "If set, the memory and CPU arguments are ignored.",
)
@click.option(
    "--version",
    "version",
    is_flag=False,
    help="Server image version [advanced]",
)
@click.option("--name", is_flag=False, help="Name to assign to the server")
@click.option(
    "--environment",
    "environments",
    multiple=True,
    help="Environments to apply to the server",
)
@click.option(
    "--wait",
    is_flag=True,
    help="Wait until the server is running before exiting.",
)
def new(
    project,
    cores,
    memory,
    type_,
    machine_type,
    version,
    name,
    environments,
    wait,
):
    """Create a new SherlockML server."""
    # pylint: disable=too-many-arguments
    _check_credentials()
    project_id = _resolve_project(project)
    environment_ids = [
        _resolve_environment(project_id, env) for env in environments
    ]

    if machine_type is None or machine_type == "custom":
        machine_type = "custom"
        milli_cpus = int(cores * 1000)
        memory_mb = int(memory * 1000)

    elif machine_type is not None and machine_type != "custom":
        milli_cpus = None
        memory_mb = None

    client = sml.galleon.Galleon()
    server_id = client.create_server(
        project_id,
        type_,
        machine_type,
        milli_cpus,
        memory_mb,
        name,
        version,
        environment_ids,
    )
    click.echo("Creating server {} in project {}".format(server_id, project))
    if wait:
        while True:
            servers = [
                server.id_
                for server in client.get_servers(project_id, status="running")
            ]
            if server_id in servers:
                break
            time.sleep(1)


@server.command()
@click.argument("project")
@click.argument("server")
def terminate(project, server):
    """Terminate a SherlockML server."""
    _check_credentials()
    _, server_id = _resolve_server(project, server, ensure_running=False)
    client = sml.galleon.Galleon()
    client.terminate_server(server_id)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("project")
@click.argument("server")
@click.argument("ssh_opts", nargs=-1, type=click.UNPROCESSED)
def shell(project, server, ssh_opts):
    """Open a shell on an SherlockML server.

    Any additional arguments given are passed on to SSH. This allows you to set
    up, for example, port forwarding:

    $ sml shell <project> <server> -L 9000:localhost:8888
    """
    _check_credentials()

    project_id, server_id = _resolve_server(project, server)
    client = sml.galleon.Galleon()
    details = client.ssh_details(project_id, server_id)

    hostname = details["hostname"]
    port = details["port"]
    username = details["username"]
    key = details["key"]

    with _save_key_to_file(key) as filename:
        cmd = (
            ["ssh"]
            + SSH_OPTIONS
            + [
                "-p",
                str(port),
                "-i",
                filename,
                "{}@{}".format(username, hostname),
            ]
        )
        cmd += list(ssh_opts)
        _run_ssh_cmd(cmd)


@cli.group()
def environment():
    """Manipulate SherlockML server environments."""
    _check_credentials()


@environment.command(name="list")
@click.argument("project")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print extra information about environments.",
)
def list_environments(project, verbose):
    """List your environments."""
    client = sml.baskerville.Baskerville()
    project_id = _resolve_project(project)
    environments = client.get_environments(project_id)
    if verbose:
        if not environments:
            click.echo("No environments.")
        else:
            click.echo(
                tabulate(
                    [(e.name, e.id_) for e in environments],
                    ("Environment Name", "ID"),
                    tablefmt="plain",
                )
            )
    else:
        for environment in environments:
            click.echo(environment.name)


@environment.command()
@click.argument("project")
@click.argument("server")
@click.argument("environment")
def apply(project, server, environment):
    """Apply an environment to the server"""
    project_id, server_id = _resolve_server(project, server)
    environment_id = _resolve_environment(project_id, environment)

    client = sml.galleon.Galleon()
    client.apply_environment(server_id, environment_id)

    click.echo(
        "Applying environment {} to server {} for project {}".format(
            environment, server, project
        )
    )


def _format_command(command):
    formatted_parts = []
    for part in command:
        if len(part.split()) > 1:
            formatted_parts.append(repr(part))
        else:
            formatted_parts.append(part)
    return " ".join(formatted_parts)


@environment.command()
@click.argument("project")
@click.argument("server")
def status(project, server):
    """Get the execution status for an environment."""
    project_id, server_id = _resolve_server(project, server)

    galleon_client = sml.galleon.Galleon()
    server = galleon_client.get_server(project_id, server_id)

    client = sml.hound.Hound(server.hound_url)
    execution = client.latest_environment_execution()

    if execution is None:
        msg = "No environment has yet been applied to this server."
        _print_and_exit(msg, 64)

    click.echo("Latest environment execution:")
    click.echo("  Status: {}".format(execution.status))
    for i, environment in enumerate(execution.environments):
        click.echo("")
        click.echo("Environment {}".format(i))
        for j, step in enumerate(environment.steps):
            click.echo("")
            click.echo("Step {}:".format(j))
            click.echo("  Status:  {}".format(step.status))
            click.echo("  Command: {}".format(_format_command(step.command)))


@environment.command()
@click.argument("project")
@click.argument("server")
@click.option(
    "--step",
    "-s",
    "step_number",
    type=int,
    help="Display only the logs for this step",
)
def logs(project, server, step_number):
    """Stream the logs for a server environment application."""
    project_id, server_id = _resolve_server(project, server)

    galleon_client = sml.galleon.Galleon()
    server = galleon_client.get_server(project_id, server_id)

    client = sml.hound.Hound(server.hound_url)
    execution = client.latest_environment_execution()

    if execution is None:
        msg = "No environment has yet been applied to this server."
        _print_and_exit(msg, 64)

    steps = [
        step
        for environment_execution in execution.environments
        for step in environment_execution.steps
    ]

    if step_number is not None:
        try:
            steps = [steps[step_number]]
        except IndexError:
            _print_and_exit("step {} out of range".format(step_number), 64)

    for step in steps:
        for line in client.stream_environment_execution_step_logs(step):
            click.echo(line)


@cli.group()
def file():
    """Manipulate files in a SherlockML project."""
    _check_credentials()


@file.command()
@click.argument("project")
@click.argument("local")
@click.argument("remote")
@click.option("--server", is_flag=False, help="Name or ID of server to use.")
def put(project, local, remote, server):
    """Copy a local file to the SherlockML workspace."""

    project_id, server_id = _resolve_server(project, server)

    client = sml.galleon.Galleon()
    details = client.ssh_details(project_id, server_id)

    escaped_remote = sml.shell.quote(remote)

    hostname = details["hostname"]
    port = details["port"]
    username = details["username"]
    key = details["key"]
    with _save_key_to_file(key) as filename:
        cmd = (
            ["scp"]
            + SSH_OPTIONS
            + [
                "-i",
                filename,
                "-P",
                str(port),
                os.path.expanduser(local),
                u"{}@{}:{}".format(username, hostname, escaped_remote),
            ]
        )
        _run_ssh_cmd(cmd)


@file.command()
@click.argument("project")
@click.argument("remote")
@click.argument("local")
@click.option("--server", is_flag=False, help="Name or ID of server to use.")
def get(project, remote, local, server):
    """Copy a file from the SherlockML workspace to the local machine."""

    project_id, server_id = _resolve_server(project, server)

    client = sml.galleon.Galleon()
    details = client.ssh_details(project_id, server_id)

    escaped_remote = sml.shell.quote(remote)

    hostname = details["hostname"]
    port = details["port"]
    username = details["username"]
    key = details["key"]
    with _save_key_to_file(key) as filename:
        cmd = (
            ["scp"]
            + SSH_OPTIONS
            + [
                "-i",
                filename,
                "-P",
                str(port),
                u"{}@{}:{}".format(username, hostname, escaped_remote),
                os.path.expanduser(local),
            ]
        )
        _run_ssh_cmd(cmd)


def _rsync(project, local, remote, server, rsync_opts, up):
    """Sync files from or to server."""

    project_id, server_id = _resolve_server(project, server)

    client = sml.galleon.Galleon()
    details = client.ssh_details(project_id, server_id)

    hostname = details["hostname"]
    port = details["port"]
    username = details["username"]
    key = details["key"]

    escaped_remote = sml.shell.quote(remote)
    if up:
        path_from = local
        path_to = u"{}@{}:{}".format(username, hostname, escaped_remote)
    else:
        path_from = u"{}@{}:{}".format(username, hostname, escaped_remote)
        path_to = local

    with _save_key_to_file(key) as filename:
        ssh_cmd = "ssh {} -p {} -i {}".format(
            " ".join(SSH_OPTIONS), port, filename
        )

        rsync_cmd = ["rsync", "-a", "-e", ssh_cmd, path_from, path_to]
        rsync_cmd += list(rsync_opts)

        _run_ssh_cmd(rsync_cmd)


@file.command(
    name="sync-up", context_settings={"ignore_unknown_options": True}
)
@click.argument("project")
@click.argument("local")
@click.argument("remote")
@click.argument("rsync_opts", nargs=-1, type=click.UNPROCESSED)
@click.option("--server", is_flag=False, help="Name or ID of server to use.")
def sync_up(project, local, remote, server, rsync_opts):
    """Sync local files up to a project with rsync.

    Arguments are used as "rsync -a LOCAL server:REMOTE [RSYNC_OPTS]".
    """
    _rsync(project, local, remote, server, rsync_opts, True)


@file.command(
    name="sync-down", context_settings={"ignore_unknown_options": True}
)
@click.argument("project")
@click.argument("remote")
@click.argument("local")
@click.argument("rsync_opts", nargs=-1, type=click.UNPROCESSED)
@click.option("--server", is_flag=False, help="Name or ID of server to use.")
def sync_down(project, remote, local, server, rsync_opts):
    """Sync remote files down from project with rsync.

    Arguments are used as "rsync -a server:REMOTE LOCAL [RSYNC_OPTS]".
    """
    _rsync(project, local, remote, server, rsync_opts, False)
