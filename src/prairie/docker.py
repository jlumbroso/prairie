import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from click_option_group import optgroup, RequiredMutuallyExclusiveOptionGroup
from click_spinner import spinner

# Setting up the docker command group
@click.group(cls=HelpColorsGroup, help_headers_color='bright_green', help_options_color='yellow')
def docker():
    """Docker related commands."""
    pass

# The run command inside the docker group
@docker.command(cls=HelpColorsCommand, help_headers_color='green', help_options_color='bright_yellow')
@optgroup.group('Run Options', cls=RequiredMutuallyExclusiveOptionGroup)
@optgroup.option('--image', '-i', type=str, help='Specify the Docker image to run.')
@optgroup.option('--container', '-c', type=str, help='Specify the Docker container to run.')
@click.option('--port', '-p', type=int, default=80, help='Specify the port to bind to.')
def run(image, container, port):
    """Run a Docker container."""
    with spinner():
        # Placeholder for the actual logic to run the Docker container
        pass
    click.secho(f"Running {image or container} on port {port}", fg='green')
