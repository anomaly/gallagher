# Installation & Usage

What you need to install will widely depend on if you are looking to use our tools, building software with our libraries or contributing to the project. This guide will get you set up for each one of the use cases. While the end user tools do not require software development experience, the other development tools are biased towards Python developers.

## Requirements

You will require Python 3.10 or above to run the SDK and tools. We provide containerised versions and binaries for most popular platforms. Please keep reading for specific instructions.

## Installation

In the most trivial cases we recommend installation via `PyPI`. The package is designed such that you only install what you need. The SDK is required by all our tools, hence it's the lowest common denominator.

The SDK can be installed by adding it as a dependency to your project:

```bash
poetry add gallagher
```

If you are feeling adventurous you can install everything by:

```bash
poetry add gallagher[all]
```

### SDK

### Command Line Interface

### Terminal User Interface

### SQL Support

## Developer Notes

This library uses [httpx](https://www.python-httpx.org) as the HTTP transport and [pydantic](https://pydantic.dev) to construct and ingest payloads. We use [taskfile](https://taskfile.dev) to run tasks. Our test suite is setup using `pytest`.

Anomaly has a demo Command Centre set up in the cloud that we run tests against. This is populate using a sample site configuration. There are no real security controllers connected to this instance. Upon a PR being lodged, Github actions is configured to run the entire test suite against our demo instance.

To contribute to the library, please fork this repository and lodge a pull request for us to accept your changes.

### Taskfile

[Task](https://taskfile.dev) is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make. Gallagher Python Toolkit uses Task to run common tasks such as testing, linting, and building the documentation. First follow the [installation steps](https://taskfile.dev/installation/) to install Task on your system.

All the `tasks` are quite logically grouped and most of them will need you to have a `virtualenv` initialised via `poetry`.

> Our Github workflows use [Task](https://taskfile.dev/installation/#github-actions) via the Github action.

Some of the `task` targets take parameters e.g.

`task test` will run the entire test suite, while `task test -- test_cardholder.py` will run only the tests in `test_cardholder.py`.

### Building the Docs

The documentation is build using [mkdocs](https://www.mkdocs.org) and hosted on [Github pages](https://anomaly.github.io/gallagher/). The project repository is configured to build and publish the documentation on every commit to the `master` branch.

Some handy commands to get you started:

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve -a localhost:8003` - Start the live-reloading docs server, `-a` allows you to provide a custom address.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

We have a wrapper for running the `mkdocs` web server at `task dev:docs` which runs the server on port `8001`.

To start contributing please fork this repository, make the changes you desire and submit a pull request for us to merge your changes in. Alternatively consider [starting a discussion](https://github.com/anomaly/gallagher/discussions) or [raising an issue](https://github.com/anomaly/gallagher/issues). Be kind to our maintainers and check to see if a similar discussion is already in place and join the thread.
