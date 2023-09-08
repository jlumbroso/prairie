import click
import loguru
from click_option_group import optgroup

from .helpers import run_prairielearn_container

@click.group()
def docker():
    """Docker related commands."""
    pass

@docker.command()
@optgroup.group('PrairieLearn Configuration', help='Configuration options for PrairieLearn.')
@click.option('--job-dir', default=None, help='Directory for jobs. If not provided, it will be determined based on other flags.')
@click.option('--force-job-dir', is_flag=True, default=False, help='Force the use of a default job directory if none is provided.')
@click.option('--course-dir', multiple=True, type=click.Path(exists=True), help='Directories for courses. Can specify multiple times.')
@click.option('--external-grader', is_flag=True, help='Enable support for external graders and workspaces.')
@click.option('--version', default="us-prod-live", help='Specify the version of PrairieLearn to run.')
@click.option('--port', default=3000, type=int, help='Specify a custom port for PrairieLearn.')
def launch(job_dir, force_job_dir, course_dir, external_grader, version, port):
    """Launch a PrairieLearn container."""
    # Determine job_dir based on flags
    if job_dir is None and (external_grader or force_job_dir):
        loguru.logger.info(f"No job directory provided. But overriding either because external graders are requested or --force-job-dir.")
        loguru.logger.info(f"Using job dir default local user path: ~/var/pl_jobs, expanded to {job_dir}.")
        job_dir = "~/var/pl_jobs"

    try:
        container = run_prairielearn_container(
            job_dir=job_dir, 
            course_dirs=list(course_dir), 
            external_grader=external_grader, 
            version=version, 
            port=port
        )
        click.echo(f"Container {container.id} started.")
    except ValueError as ve:
        loguru.logger.error(ve)
        click.echo(f"Error: {ve}")
    except FileNotFoundError as fe:
        loguru.logger.error(fe)
        click.echo(f"Error: {fe}")

@docker.command()
def update():
    """Update to the latest version of PrairieLearn."""
    client = docker.from_env()
    client.images.pull("prairielearn/prairielearn:us-prod-live")
    click.echo("Updated to the latest version of PrairieLearn.")
