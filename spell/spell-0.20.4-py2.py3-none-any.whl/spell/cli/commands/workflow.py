# -*- coding: utf-8 -*-
import click
import os

from spell.cli.commands.logs import logs
from spell.cli.commands.run import create_run_request
from spell.cli.exceptions import (
    api_client_exception_handler,
    ExitException,
    SPELL_INVALID_CONFIG,
)
from spell.cli.log import logger
from spell.cli.utils import git_utils, parse_utils, with_emoji, ellipses


@click.command(name="workflow",
               short_help="Execute a new workflow")
@click.argument("command")
@click.argument("args", nargs=-1)
@click.option("--local", is_flag=True,
              help="Execute command locally instead of remotely on Spell's infrastructure")
@click.option("-r", "--repo", "repo_paths", multiple=True, metavar="LABEL=PATH[:COMMIT_HASH]",
              help="Add a git repository at a specific commit to this workflow by specifying LABEL=PATH, where PATH is "
                   "a path to a local git repository on disk and NAME is a label to refer to "
                   "this commit in future run requests. COMMIT_HASH can optionally be specified "
                   "by LABEL=PATH[:COMMIT_HASH]. "
                   "If no COMMIT_HASH is specified, the currently checked out commit of the repo will be used.")
@click.option("--pip", "pip_packages",
              help="Single dependency to install using pip", multiple=True)
@click.option("--pip-req", "requirements_file",
              help="Requirements file to install using pip")
@click.option("--apt", "apt_packages",
              help="Dependency to install using apt", multiple=True)
@click.option("--from", "docker_image",
              help="Dockerfile on docker hub to run from")
@click.option("--python2", is_flag=True,
              help="set python version to python 2")
@click.option("--python3", is_flag=True,
              help="set python version to python 3 (default)")
@click.option("--conda-env", help="Name of conda environment name to activate. "
                                  "If omitted but --conda-file is specified then it is "
                                  "assumed that --conda-file is an 'explicit' env file.")
@click.option("--conda-file",
              help="Path to conda environment file, defaults to ./environment.yml "
                   "when --conda-env is specified",
              type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True),
              default=None)
@click.option("-b", "--background", is_flag=True,
              help="Do not print logs")
@click.option("-c", "--commit-ref", default="HEAD",
              help="Git commit hash to run")
@click.option("-d", "--description", default=None,
              help="Description of the run. If unspecified defaults to the current commit message")
@click.option("-e", "--env", "envvars", multiple=True,
              help="Add an environment variable to the run")
@click.option("-f", "--force", is_flag=True,
              help="Skip interactive prompts")
@click.option("-v", "--verbose", is_flag=True,
              help="Print additional information")
@click.pass_context
def workflow(ctx, command, args, local, repo_paths,
             pip_packages, requirements_file, apt_packages, docker_image,
             python2, python3, commit_ref, description, envvars, background,
             conda_env, conda_file, force, verbose, **kwargs):
    """
    Execute WORKFLOW either remotely or locally

    The workflow command is used to create workflows which manage other runs.
    Complex machine learning applications often require multi-stage pipelines
    (e.g., data loading, transforming, training, testing, iterating). Workflows
    are designed to help you automate this process. While a workflow executes
    much like a normal run, it is capable of launching other runs that are
    all associated with each other. A workflow must specify every git commit that
    will be used by the given workflow script using the `--repo` flag.
    The various other options can be used to customize the environment that the
    workflow script runs in.
    """
    run_req = None
    try:
        repo_paths = parse_utils.parse_repos(repo_paths)
    except parse_utils.ParseException as e:
        raise ExitException(click.wrap_text(
            "Incorrect formatting of repo '{}', it must be "
            "<repo_name>=<repo_path>[:commit_ref]".format(e.token)),
            SPELL_INVALID_CONFIG)
    workspace_specs = git_utils.sync_repos(ctx, repo_paths, force)

    if not local:
        run_req = create_run_request(
            ctx=ctx,
            command=command,
            args=args,
            machine_type="CPU",
            pip_packages=pip_packages,
            requirements_file=requirements_file,
            apt_packages=apt_packages,
            docker_image=docker_image,
            framework=None,
            python2=python2,
            python3=python3,
            commit_ref=commit_ref,
            description=description,
            envvars=envvars,
            raw_resources=[],
            background=background,
            conda_env=conda_env,
            conda_file=conda_file,
            force=force,
            verbose=verbose,
            local_caching=False,
            idempotent=False,
            run_type="workflow")

    client = ctx.obj["client"]
    logger.info("sending workflow request to api")
    with api_client_exception_handler():
        workflow = client.workflow(run_req, workspace_specs)

    utf8 = ctx.obj["utf8"]
    click.echo(with_emoji(u"💫", "Casting workflow #{}".format(workflow.id) + ellipses(utf8), utf8))
    if not local:
        if background:
            click.echo("View logs with `spell logs {}`".format(workflow.managing_run.id))
        else:
            click.echo(with_emoji(u"✨", "Following workflow at run {}.".format(workflow.managing_run.id), utf8))
            click.echo(with_emoji(u"✨", "Stop viewing logs with ^C", utf8))
            ctx.invoke(logs, run_id=str(workflow.managing_run.id), follow=True, verbose=verbose)
    else:
        os.environ["SPELL_WORKFLOW_ID"] = str(workflow.id)
        os.system(" ".join(("'{}'".format(x) for x in (command,) + args)))
