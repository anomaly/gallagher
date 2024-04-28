# Welcome to Gallagher Python Toolkit

Gallagher Python Toolkit aims to enhance the developer experience of working with Gallagher Security's Command Centre.

> **Note:** This project is not affiliated with Gallagher in any way.

## History

This project maintains an idiomatic client for Python. The project began as a requirement for us to reliably work with the Gallagher API. While Gallagher publish their [API reference](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html) which is built from an OpenAPI spec with [Spectacle](https://github.com/sourcey/spectacle) documentation generator flavours. The OpenAPI spec is maintained by hand and [can be found on Github](https://github.com/GallagherSecurity/cc-rest-docs/tree/master/swagger).

Our assumption is that this is for security and technical reasons. In the spirit of building good quality software we embarked on building a Python idiomatic client with full test coverage.

The API client draws inspiration from companies like [Stripe](https://stripe.com) or projects like [pyndatic](https://pydantic.dev) who are known for stellar developer experience. Our aim is to provide a similar quality of developer experience for Gallagher projects.

The design pattern of the API client is opinionated from our experience as software engineers. We goto great lengths to document and justify our thought process so others can see where we are coming from.

## Features

- pydantic models for all API payloads
- HTTP transport using httpx
- Full test coverage
- A completely python based interface to interacting with Gallagher Command Centre

Additionally we offer:

- A command line interface to interact with the command centre
- A terminal user interface with some nifty features

## Developing the client

This library uses [httpx](https://www.python-httpx.org) as the HTTP transport and [pydantic](https://pydantic.dev) to construct and ingest payloads. We use [taskfile](https://taskfile.dev) to run tasks. Our test suite is setup using `pytest`.

Anomaly has a demo Command Centre set up in the cloud that we run tests against. This is populate using a sample site configuration. There are no real security controllers connected to this instance. Upon a PR being lodged, Github actions is configured to run the entire test suite against our demo instance.

To contribute to the library, please fork this repository and lodge a pull request for us to accept your changes.

## Contributing to the documentation

The documentation is build using [mkdocs](https://www.mkdocs.org) and hosted on [Github pages](https://anomaly.github.io/gallagher/). The project repository is configured to build and publish the documentation on every commit to the `master` branch.

Some handy commands to get you started:

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve -a localhost:8003` - Start the live-reloading docs server, `-a` allows you to provide a custom address.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

To start contributing please fork this repository, make the changes you desire and submit a pull request for us to merge your changes in. Alternatively consider [starting a discussion](https://github.com/anomaly/gallagher/discussions) or [raising an issue](https://github.com/anomaly/gallagher/issues). Be kind to our maintainers and check to see if a similar discussion is already in place and join the thread.
