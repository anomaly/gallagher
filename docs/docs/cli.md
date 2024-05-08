# Command Line Interface

We provide a command line interface to interact with the Gallagher Command Centre. It uses the API client to communicate with the server, which doubly serves as a reference example of how to use the API client.

> We use [typer](https://typer.tiangolo.com) to construct the CLI, which in turn uses [click](https://click.palletsprojects.com). We also use [rich](https://rich.readthedocs.io/en/stable/) to make the output nicer. The CLI is decoupled from the API client, and is not install by default.

We follow a `git` like `command`, `sub-command` pattern, so it should feel quite familiar.

poetry will install the alias `gal` for you to interact with the CLI. You can ask for help with:

::: mkdocs-typer
    :module: gallagher.cli
    :command: app

## Resources

- [Command Line Interface Guidelines - clig.dev](https://clig.dev)