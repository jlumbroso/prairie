import os

import click
import click_help_colors
import click_option_group
import docker as docker_sdk
import loguru

from . import helpers

@click.group(cls=click_help_colors.HelpColorsGroup, help_headers_color='green', help_options_color='bright_yellow')
def docker():
    """Docker related commands."""
    loguru.logger.info("Executing Docker related commands.")
    helpers.log_docker_env()

    # Check to see if Docker host is empty
    if helpers.set_docker_host():
        loguru.logger.warning("Docker host was not set, tried to correct")
        helpers.log_docker_env()


@docker.command()
@click.option('--course-dir', required=True, multiple=True, type=click.Path(exists=True), help='📁 Directories for courses. Can specify multiple times. (Mandatory)')
@click_option_group.optgroup.group('Optional PrairieLearn Configuration', help='')
@click_option_group.optgroup.option('--job-dir', default=None, help='📁 Directory for jobs. If not provided, it will be determined based on other flags.')
@click_option_group.optgroup.option('--force-job-dir', is_flag=True, default=False, help='🔄 Force the use of a default job directory if none is provided.')
@click_option_group.optgroup.option('--external-grader', is_flag=True, help='⚙️  Enable support for external graders and workspaces.')
@click_option_group.optgroup.option('--version', default="us-prod-live", help='🔄 Specify the version of PrairieLearn to run.')
@click_option_group.optgroup.option('--port', default=3000, type=int, help='📡  Specify a custom port for PrairieLearn.')
def launch(job_dir, force_job_dir, course_dir, external_grader, version, port):
    """🚀 Launch a PrairieLearn container."""
    loguru.logger.info("Attempting to launch a PrairieLearn container.")
    
    # Determine job_dir based on flags
    if job_dir is None and (external_grader or force_job_dir):
        loguru.logger.info(f"No job directory provided. But overriding either because external graders are requested or --force-job-dir.")
        loguru.logger.info(f"Using job dir default local user path: ~/var/pl_jobs, expanded to {job_dir}.")
        job_dir = "~/var/pl_jobs"

    try:
        container = helpers.run_prairielearn_container(
            job_dir=job_dir, 
            course_dirs=list(course_dir), 
            external_grader=external_grader, 
            version=version, 
            port=port
        )
        click.echo(f"Container {container.id} started successfully.")
        loguru.logger.info(f"Container {container.id} started successfully.")
    except ValueError as ve:
        loguru.logger.error(f"ValueError encountered: {ve}")
        click.echo(f"Error: {ve}")
    except FileNotFoundError as fe:
        loguru.logger.error(f"FileNotFoundError encountered: {fe}")
        click.echo(f"Error: {fe}")

@docker.command()
def update():
    """Update to the latest version of PrairieLearn."""
    loguru.logger.info("Attempting to update to the latest version of PrairieLearn.")
    client = docker_sdk.from_env()
    client.images.pull("prairielearn/prairielearn:us-prod-live")
    click.echo("Updated to the latest version of PrairieLearn.")
    loguru.logger.info("Successfully updated to the latest version of PrairieLearn.")

@docker.command()
def status():
    """🔍 Check the status of a running PrairieLearn container."""
    loguru.logger.info("Checking the status of PrairieLearn container.")
    import docker
    client = docker.from_env()
    containers = [c for c in client.containers.list(all=True) if "prairielearn/prairielearn" in c.image.tags[0]]
    
    if not containers:
        click.echo("No PrairieLearn container is currently running.")
        return

    for container in containers:
        status = container.status
        image = container.image.tags[0] if container.image.tags else "Unknown"
        ports = container.ports
        mounts = container.attrs['Mounts']
        
        click.echo(click.style(f"Container ID: {container.id}", bold=True, fg="green"))
        click.echo(f"Status: {status}")
        click.echo(f"Image: {image}")
        
        if ports:
            for private_port, port_bindings in ports.items():
                for binding in port_bindings:
                    click.echo(f"Port: {private_port} binded to {binding['HostPort']}")
        
        if mounts:
            click.echo(click.style("Course Directories and Mount Points:", bold=True, fg="yellow"))
            for mount in mounts:
                if "course" in mount['Destination']:
                    click.echo(click.style(f"• {mount['Source']} -> {mount['Destination']}", fg="blue"))
        
        click.echo("--------------------------------------------------")

    # Interpretation
    click.echo(click.style("\nInterpretation:", bold=True, fg="cyan"))
    click.echo("• Your PrairieLearn instance is currently running.")
    if ports:
        for _, port_bindings in ports.items():
            for binding in port_bindings:
                click.echo(f"• You can access it at: " + click.style(f"https://localhost:{binding['HostPort']}", bold=True, fg="blue"))
    else:
        click.echo("• No ports found for the running PrairieLearn instance.")
    click.echo("• The courses you've mounted are highlighted above in blue.")


