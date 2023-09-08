import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from click_option_group import optgroup, RequiredMutuallyExclusiveOptionGroup

from . import __version__
from . import docker  # Modified this line for a relative import

# Setting up the main command group with a description
@click.group(cls=HelpColorsGroup, help_headers_color='green', help_options_color='bright_yellow')
@click.version_option(version=__version__, prog_name='prairie')
def cli():
    """Prairie: A command line interface for PrairieLearn.

    This tool provides utilities to streamline your PrairieLearn experience.
    """
    pass

# Adding the docker command group
cli.add_command(docker.docker)

if __name__ == '__main__':
    cli()
