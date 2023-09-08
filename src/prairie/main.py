import click
import click_help_colors
import loguru

from . import __version__, docker

@click.group(cls=click_help_colors.HelpColorsGroup, help_headers_color='green', help_options_color='bright_yellow')
@click.version_option(version=__version__, prog_name='prairie')
def cli():
    """Prairie: A command line interface for PrairieLearn.

    This tool provides utilities to streamline your PrairieLearn experience.
    """
    loguru.logger.info("Prairie CLI started.")

cli.add_command(docker.docker)

if __name__ == '__main__':
    cli()
