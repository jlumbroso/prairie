# Prairie CLI

Prairie CLI is a command-line interface designed to streamline your PrairieLearn experience. Whether you're a course instructor, a content developer, or just someone looking to explore PrairieLearn, this tool offers utilities to make your journey smoother.

## Features

* Docker Integration: Easily manage PrairieLearn containers with built-in Docker commands.
* Local Course Development: Test and develop your course content locally without the need for external setups.
* Easy Updates: Keep your local PrairieLearn version up-to-date with simple commands.

## Installation

1. Dependencies: Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
2. (Windows Users): It's recommended to use WSL 2 for optimal performance. Follow the [installation guide](https://learn.microsoft.com/en-us/windows/wsl/install) for WSL 2 and integrate it with Docker as described [here](https://docs.docker.com/desktop/windows/wsl/).
3. Install Prairie CLI: (Installation steps for Prairie CLI would go here)

## Usage

Once installed, you can use the `prairie` command to access all features. Here are some common commands:

* Launch PrairieLearn: `prairie docker launch --course-dir YOUR_COURSE_DIRECTORY`
* Update PrairieLearn: `prairie docker update`
* Check PrairieLearn Status: `prairie docker status`

For a full list of commands and options, use `prairie --help`.

## Contributing

If you'd like to contribute to Prairie CLI, just make a pull request.

## License

This project is licensed [under the LGPLv3 license](https://www.gnu.org/licenses/lgpl-3.0.en.html),
with the understanding that importing a Python modular is similar in spirit to dynamically linking
against it.

- You can use the library/CLI `prairie` in any project, for any purpose,
  as long as you provide some acknowledgement to this original project for
  use of the library (for open source software, just explicitly including
  `prairie` in the dependency such as a `pyproject.toml` or `Pipfile`
  is acknowledgement enough for me!).

- If you make improvements to `prairie`, you are required to make those
  changes publicly available.

This license is compatible with the license of all the dependencies as
documented in [this project's own `pyproject.toml`](https://github.com/jlumbroso/prairie/blob/master/pyproject.toml#L29-L49).
