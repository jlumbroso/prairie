import os

import docker
import loguru

def run_docker_container(
    image_name: str,
    command: str = None,
    ports: dict = None,
    volumes: dict = None,
    environment: dict = None,
    remove: bool = True,
    tty: bool = True,
    stdin_open: bool = True,
    detach: bool = True
) -> docker.models.containers.Container:
    """
    Run a Docker container using the specified parameters.
    """
    loguru.logger.info(f"Attempting to run Docker container with image: {image_name}")
    
    # Create a Docker client
    client = docker.from_env()

    # Pull the image
    client.images.pull(image_name)
    loguru.logger.debug(f"Pulled image: {image_name}")

    # Run the container
    container = client.containers.run(
        image=image_name,
        command=command,
        ports=ports,
        volumes=volumes,
        environment=environment,
        remove=remove,
        tty=tty,
        stdin_open=stdin_open,
        detach=detach
    )

    loguru.logger.info(f"Container with ID {container.id} started successfully.")
    return container

def run_prairielearn_container(
    job_dir: str = None, 
    course_dirs: tuple = None, 
    external_grader: bool = False, 
    version: str = "us-prod-live", 
    port: int = 3000
) -> docker.models.containers.Container:
    """
    Run a PrairieLearn container with specific configurations.
    """
    loguru.logger.info("Attempting to run a PrairieLearn container with specific configurations.")
    
    # Resolve user's home directory
    home_dir = os.path.expanduser("~")

    # Check if course_dirs is provided
    if not course_dirs:
        loguru.logger.error("The course directories are not provided.")
        raise ValueError("At least one course directory is required.")

    # Log the number of courses added
    loguru.logger.info(f"{len(course_dirs)} course(s) added: {', '.join(course_dirs)}")

    # Check if more than 9 courses are added
    if len(course_dirs) > 9:
        ignored_courses = course_dirs[9:]
        loguru.logger.warning(f"More than 9 courses added. Ignoring courses: {', '.join(ignored_courses)}")
        course_dirs = course_dirs[:9]

    # Set up parameters for the PrairieLearn container
    image_name = f"prairielearn/prairielearn:{version}"
    ports = {str(port): port}
    volumes = {}
    environment = {}

    # If job_dir is provided, set it up
    if job_dir:
        volumes[job_dir] = {'bind': '/jobs', 'mode': 'rw'}
        environment['HOST_JOBS_DIR'] = job_dir

        # Check existence of job directory and create if necessary
        if not os.path.exists(job_dir):
            loguru.logger.info(f"{job_dir} is requested as job dir but does not exist, attempting to create it.")
            os.makedirs(job_dir)

    # Set up course directories
    for idx, course_dir in enumerate(course_dirs, start=1):
        if not os.path.exists(course_dir):
            loguru.logger.error(f"The course directory '{course_dir}' does not exist.")
            raise FileNotFoundError(f"The course directory '{course_dir}' does not exist.")
        mount_point = f"/course{'' if idx == 1 else idx}"
        volumes[course_dir] = {'bind': mount_point, 'mode': 'rw'}

    # If external grader is enabled, add necessary configurations
    if external_grader:
        volumes["/var/run/docker.sock"] = {'bind': '/var/run/docker.sock', 'mode': 'rw'}
        environment["HOST_JOBS_DIR"] = job_dir

    # Run the container
    container = run_docker_container(
        image_name=image_name,
        ports=ports,
        volumes=volumes,
        environment=environment
    )

    loguru.logger.info(f"PrairieLearn container with ID {container.id} started successfully.")
    return container
