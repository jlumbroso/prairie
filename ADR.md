# Architecture Decision Records

This document contains the Architecture Decision Records (ADRs) for the PrairieLearn CLI, which are used to document the architectural decisions made during the development process and the reasons behind them.

## ADR 001: Use of `click` library for CLI development

**Title:** Adopting `click` library for CLI development

**Status:** Accepted

**Context:** The `click` library provides a simple way to write command-line interfaces from Python code. It offers argument parsing, colorized output, and other utilities that simplify CLI development.

**Decision:** Use the `click` library to develop the PrairieLearn CLI to streamline the development process and provide a consistent user experience.

**Consequences:**
- Simplified argument parsing and command structuring.
- Consistent and colorized output for better user experience.
- Dependency on an external library.

---

## ADR 002: Use of `loguru` for logging

**Title:** Adopting `loguru` for logging

**Status:** Accepted

**Context:** Logging is essential for debugging and monitoring the behavior of the CLI. `loguru` offers a straightforward way to set up logging with minimal configuration.

**Decision:** Use `loguru` for logging in the PrairieLearn CLI to ensure consistent logging behavior and simplify the setup.

**Consequences:**
- Simplified logging setup with minimal configuration.
- Consistent logging format and behavior.
- Dependency on an external library.

---

## ADR 003: Implementing verbosity flag for logging levels

**Title:** Introducing a verbosity flag for controlling logging levels

**Status:** Accepted

**Context:** Different users and use-cases might require different levels of logging verbosity. A flag allows users to control the verbosity of the logs easily.

**Decision:** Implement a `-v` flag in the PrairieLearn CLI, where `-v` sets the log level to `INFO` and `-vv` sets it to `DEBUG`.

**Consequences:**
- Users can control the verbosity of the logs.
- The default log level is set to `WARNING` to avoid excessive logging.
- Additional code and logic to handle the verbosity levels.

---

## ADR 004: Docker integration for PrairieLearn CLI

**Title:** Integrating Docker commands within the PrairieLearn CLI

**Status:** Accepted

**Context:** PrairieLearn can be run locally using Docker. Integrating Docker commands within the CLI simplifies the process of launching and managing PrairieLearn containers.

**Decision:** Integrate Docker-related commands within the PrairieLearn CLI, allowing users to launch, update, and check the status of PrairieLearn containers directly from the CLI.

**Consequences:**
- Simplified process for users to run PrairieLearn locally.
- Dependency on Docker being installed on the user's machine.
- Additional code and logic to handle Docker commands and interactions.

---

## ADR 005: External Grader and Workspace Support for PrairieLearn CLI

**Title:** Supporting external graders and workspaces in the PrairieLearn CLI

**Status:** Accepted

**Context:** PrairieLearn has support for external graders and workspaces. When developing questions locally, there's a need to run external grading jobs and workspaces with some workarounds.

**Decision:** Implement support for external graders and workspaces in the PrairieLearn CLI, allowing users to run external grading jobs locally using Docker.

**Consequences:**
- Users can test and develop questions with external grading support locally.
- Additional complexity in setting up and managing Docker containers for external grading.
- Dependency on specific directory structures and environment variables for external grading.

---

