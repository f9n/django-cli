import click

from . import __version__
from .core import find_manage_py, run_manage_py_with_arguments


@click.group()
@click.option("--debug", is_flag=True, help="Activate debug mode")
@click.pass_context
def main(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    if debug:
        click.echo("Debug is on")


@main.command()
def version():
    """print django-cli version"""
    click.echo("django-cli %s" % __version__)


@main.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def original(ctx):
    """finds manage.py file and then pass arguments"""
    filepath = find_manage_py()
    if ctx.obj["DEBUG"]:
        click.echo(filepath)

    run_manage_py_with_arguments(filepath, ctx.args)


if __name__ == "__main__":
    main()
