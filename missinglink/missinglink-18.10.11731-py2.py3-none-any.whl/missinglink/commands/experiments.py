# -*- coding: utf8 -*-
import click
import json
from missinglink.commands.commons import output_result
from missinglink.core.api import ApiCaller
from missinglink.commands.utilities.formatters import format_datetime, truncate_long_text, truncate_short_text
import six

from missinglink.commands.utilities.options import CommonOptions, ExperimentsOptions, ChartsOptions


def chart_name_to_id(chart_name):
    from hashlib import sha256
    # noinspection PyArgumentEqualDefault
    return sha256(six.text_type(chart_name).encode('utf-8').lower().strip()).hexdigest()


@click.group('experiments')
def experiments_commands():
    pass


@experiments_commands.command('logs')
@CommonOptions.project_id_option(required=True)
@CommonOptions.experiment_id_option()
@click.option('--disable-colors', is_flag=True, required=False)
@click.pass_context
def xp_logs(ctx, project, experiment, disable_colors):
    from missinglink.commands.utils import monitor_logs

    url = 'projects/{project_id}/experiments/{experiment_id}/logs'.format(project_id=project, experiment_id=experiment)

    monitor_logs(ctx, url, disable_colors)


@experiments_commands.command('list')
@CommonOptions.project_id_option(required=True)
@click.pass_context
def list_experiments(ctx, project):
    """List experiments of a project.
    """

    experiments = []

    def remove_prefix(name, prefix):
        if name.startswith(prefix):
            return name[:len(name)]

        return name

    def get_fields_names():
        fields = set()

        for experiment in new_experiments:
            if 'values' not in experiment:
                continue

            for value in experiment['values']:
                name = value['key']

                name = remove_prefix(name, 'ml_train_')
                name = remove_prefix(name, 'ml_')

                fields.add(name)

                experiment[name] = value['val']

            del experiment['values']

        displayed_fields.extend(fields)

    displayed_fields = ['experiment_id', 'created_at', 'display_name', 'description']

    cursor_token = None
    while True:
        list_experiments_path = 'projects/{project_id}/experiments'.format(project_id=project)

        if cursor_token:
            list_experiments_path += '?cursor_token={cursor_token}'.format(cursor_token=cursor_token)

        result = ApiCaller.call(ctx.obj, ctx.obj.session, 'get', list_experiments_path)
        cursor_token = result.get('next_experiments_token', '')
        new_experiments = result.get('experiments', [])
        experiments.extend(new_experiments)

        get_fields_names()

        if len(new_experiments) == 100:
            continue

        break

    formatters = {
        'created_at': format_datetime,
        'display_name': truncate_short_text,
        'description': truncate_long_text,
    }
    output_result(ctx, experiments, displayed_fields, formatters=formatters)


@experiments_commands.command('update-metrics')
@CommonOptions.project_id_option()
@CommonOptions.experiment_id_option()
@ExperimentsOptions.model_weights_hash_option()
@ExperimentsOptions.metrics_option(required=True)
@click.pass_context
def update_metrics(ctx, project, experiment, weights_hash, metrics):
    """Send external metrics in the experiment level.

    There are 2 ways to identify the experiment: (1) specify both `--project_id` and `--experiment_id`
    options or (2) specify `--weights-hash` option. When the model's weights hash is specified,
    ml would look up the experiment that the model belongs to.

    When both `--project_id` and `--experiment_id` are specified, the `--weights-hash` option is ignored.

    Example:

    To send metrics to the 5th experiment of the project "123", run

    \b
        ml experiments update_metrics --project_id 123 --experiment_id 5 --metrics '{"ex_cost": 99}'

    Or assuming that the model's weights hash "324e16b5e" was generated by this experiment at certain
    epoch or iteration, run

    \b
        ml experiments update_metrics --weights-hash 324e16b5e --metrics '{"ex_cost": 99}'
    """

    update_metrics_path = get_submit_path('projects/{project_id}/experiments/{experiment_id}/metrics', 'model_weights_hashes/{model_weights_hash}/metrics?experiment_only=1', project, experiment, weights_hash)
    data = _get_metrics_json(metrics)
    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'post', update_metrics_path, data)
    output_result(ctx, result, ['ok'])


def get_submit_path(by_project_and_experiment_path, by_model_hash_path, project_id, experiment_id, model_weights_hash, **kwargs):
    def raise_data_missing_error():
        if project_id is not None:
            raise click.BadOptionUsage('Please also specify --experiment option.')
        elif experiment_id is not None:
            raise click.BadOptionUsage('Please also specify --project option.')
        else:
            raise click.BadOptionUsage('Please specify the experiment using (1) --project and --experiment options or (2) --weights-hash options.')

    if project_id is not None and experiment_id is not None:
        return by_project_and_experiment_path.format(project_id=project_id, experiment_id=experiment_id, **kwargs)
    elif model_weights_hash is not None:
        return by_model_hash_path.format(model_weights_hash=model_weights_hash, **kwargs)
    raise_data_missing_error()


def _read_norm_y_values(ys):
    res = []
    dimmention_count = None

    for y in ys:
        if not isinstance(y, list):
            y = [y]
        cur_dim = len(y)
        dimmention_count = dimmention_count or cur_dim
        if dimmention_count != cur_dim:
            raise click.BadOptionUsage("All of the data values arrays must be of the same size")
        res += y
    return res


def _read_norm_x_values(xs):
    res = []
    for opt_type, suffix in [(float, '_float'), (six.integer_types, '_int'), (six.string_types, '_str')]:
        for x in xs:
            if not isinstance(x, opt_type):
                res = []
                break
            res.append(x)
        if len(res) == len(xs):
            return res, suffix
    raise click.BadOptionUsage('X values must be consistent')


def _get_metrics_json(metrics_string):
    try:
        return json.loads(metrics_string)
    except ValueError:
        raise click.BadParameter('The supplied sting is not a valid JSON dictionary format.')


@experiments_commands.command('update-chart')
@ExperimentsOptions.model_weights_hash_option()
@CommonOptions.project_id_option()
@CommonOptions.experiment_id_option()
@ChartsOptions.chart_name_option(required=True)
@ChartsOptions.chart_x_name_option()
@ChartsOptions.chart_y_name_option()
@ChartsOptions.chart_scope_option()
@ChartsOptions.chart_type_option()
@ChartsOptions.chart_x_option()
@ChartsOptions.chart_y_option()
@click.pass_context
def update_chart(ctx, weights_hash, project, experiment, chart_name, chart_scope, chart_type, chart_x_name, chart_y_name, chart_x, chart_y):
    """Send experiment external chart to an experiment.

    There are 2 ways to identify the experiment: (1) specify both `--project_id` and `--experiment_id`
    options or (2) specify `--weights-hash` option. When the model's weights hash is specified,
    ml would look up the experiment that the model belongs to.

    When both `--project_id` and `--experiment` are specified, the `--weights-hash` option is ignored.

    To send chart to the 5th experiment "precision recall" chart of the project "123" in the validation scope, run

    \b
        ml experiments updateChart --project_id 123 --experiment_id 321  --chartName "precision recall" --chartScope validation  --chartX '[0.1,0.5,0.8]' --chartY '[0.9,0.5,0.2]' --chartXNname "Precision" --chartYName "Recall"

    Or send a chart with multiple y charts:
        ml experiments updateChart --p 123 --e 321  -c "precision recall" -cs validation  -cx '[0.1,0.5,0.8]' -cy '[[0.9, 0.5],[0.5,0.25],[0.2,0.4]' --chartYName '["Func1","Func2"]'

    """
    chart_id = chart_name_to_id(chart_name)

    update_chart_path = get_submit_path(
        'projects/{project_id}/experiments/{experiment_id}/chart/{chart_id}',
        'model_weights_hashes/{model_weights_hash}/chart/{chart_id}',
        project, experiment, weights_hash, chart_id=chart_id)

    x, x_suffix = _read_norm_x_values(_get_metrics_json(chart_x))

    y = _read_norm_y_values(_get_metrics_json(chart_y))
    y_name = chart_y_name

    if y_name.startswith('['):
        y_name = _get_metrics_json(y_name)

    if not isinstance(y_name, list):
        y_name = [y_name]

    chart_legends = [chart_x_name] + y_name
    if len(y) % len(x) is not 0:
        raise click.BadOptionUsage('X and Y arrays must be of the same size')

    data = {
        'name': chart_name,
        'labels': chart_legends,
        'x' + x_suffix: x,
        'y_data': y,
        'chart': chart_type,
        'scope': chart_scope
    }

    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'put', update_chart_path, data)
    output_result(ctx, result, ['ok'])


@experiments_commands.command('update-metrics-per-iteration')
@ExperimentsOptions.model_weights_hash_option(required=True)
@ExperimentsOptions.metrics_option(required=True)
@click.pass_context
def update_model_metrics(ctx, weights_hash, metrics):
    """
    Send external metrics for a specific iteration.
    Using this option you can create a graph of the metrics for each iteration.
    The experiment and iterations are obtained from the weighted hash.

    Each model weights hash is attached to certain experiment epochs and thus can be used to send
    metrics that are relevant to those epochs. The model weights hash is a hexadecimal string. To
    calculate the weights hash of a model:

        - Calculate the sha1 strings of the weights for each layers

        - Calculate the sha1 string of the combine hashes.
            For example, the model has 3 layers with the layers' weight hashes: ['abc', '123', 'def'], the model weight hash is `sha1('abc123def')`

    WARNING: The same model weights hash can appear in different experiments or different epochs
    (for example, when running the same net twice). As such, this command will send the metrics to
    all these experiments/epochs that it can identify from the hash.

    Example:

    To send metrics of the model which hash is 324e16b5e, run

    \b
        ml experiments updateMetricsPerIteration --weights-hash 324e16b5e --metrics '{"ex_cost": 99}'

    """
    update_model_metrics_path = 'model_weights_hashes/{model_weights_hash}/metrics' \
        .format(model_weights_hash=weights_hash)
    data = _get_metrics_json(metrics)

    result = ApiCaller.call(ctx.obj, ctx.obj.session, 'post', update_model_metrics_path, data)
    output_result(ctx, result, ['ok'])
