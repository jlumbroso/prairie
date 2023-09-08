import os
import platform
import sys

import click
import click_help_colors
import loguru

from . import __version__, docker

# Define a callback to handle the verbosity level
def set_log_level(ctx, param, value):
    levels = [loguru.logger.level("WARNING"), loguru.logger.level("INFO"), loguru.logger.level("DEBUG")]
    loguru.logger.remove()
    loguru.logger.add(sys.stderr, level=levels[value].no)
    level = levels[value]
    level_value = level.no
    level_name = level.name
    loguru.logger.info(f"Set log level to {level_name}")
    return level_value

# New function to detect if the user is on Windows with WSL 2
def is_wsl2():
    flag = (os.sys.platform == 'linux' and "microsoft" in platform.uname().release.lower())
    loguru.logger.debug(f"Detected WSL 2: {flag}")
    return flag

# New function to detect if the user is on MacOS with "Apple Silicon"
def is_apple_silicon():
    flag = (platform.system() == 'Darwin' and platform.machine() == 'arm64')
    loguru.logger.debug(f"Detected Apple Silicon: {flag}")
    return flag

@click.group(cls=click_help_colors.HelpColorsGroup, help_headers_color='green', help_options_color='bright_yellow')
@click.version_option(version=__version__, prog_name='prairie')
@click.option('-v', '--verbose', count=True, callback=set_log_level, expose_value=False, is_eager=True, help="Increase verbosity level (e.g., -v or -vv).")
def cli():
    """Prairie: A command line interface for PrairieLearn.

    This tool provides utilities to streamline your PrairieLearn experience.
    """
    loguru.logger.info("Prairie CLI started.")

cli.add_command(docker.docker)

if __name__ == '__main__':
    cli()
