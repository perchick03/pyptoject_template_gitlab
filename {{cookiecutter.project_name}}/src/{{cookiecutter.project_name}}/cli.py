import sys
import click

try:
    from {{cookiecutter.project_name}} import __version__
except ModuleNotFoundError:
    print('ModuleNotFoundError: {{cookiecutter.project_name}} not found, make sure {{cookiecutter.project_name}} is install using pip install -e .', file=sys.stderr)
    exit(1)


class CliCtx:
    def __init__(self):
        self.verbose = False


pass_ctx = click.make_pass_decorator(CliCtx, ensure=True)


@click.command()
@click.option('--verbose', is_flag=True, help='Enables verbose mode.')
@click.version_option(version=__version__)
@pass_ctx
def cli(ctx: CliCtx, verbose: bool):
    ctx.verbose = verbose
    click.echo(click.style('Hello {{cookiecutter.project_name}}!', fg='bright_blue', bold=True))
    click.echo('{{cookiecutter.project_name}} == ' + __version__)


if __name__ == '__main__':
    cli()