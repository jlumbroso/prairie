import click
from click_help_colors import HelpColorsGroup

from . import __version__
from .docker import docker

@click.group(cls=HelpColorsGroup, help_headers_color='green', help_options_color='bright_yellow')
@click.version_option(version=__version__, prog_name='prairie')
def cli():
    """Prairie: A command line interface for PrairieLearn.

    This tool provides utilities to streamline your PrairieLearn experience.
    """
    pass

cli.add_command(docker)

if __name__ == '__main__':
    cli()
