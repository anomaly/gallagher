# Command Line Interface

We provide a command line interface to interact with the Gallagher Command Centre. It uses the API client to communicate with the server, which doubly serves as a reference example of how to use the API client.

> We use [typer](https://typer.tiangolo.com) to construct the CLI, which in turn uses [click](https://click.palletsprojects.com). We also use [rich](https://rich.readthedocs.io/en/stable/) to make the output nicer. The CLI is decoupled from the API client, and is not install by default.

We follow a `git` like `command`, `sub-command` pattern, so it should feel quite familiar.

poetry will install the alias `gal` for you to interact with the CLI. You can ask for help with:

```
gal --help
```

which will list the available commands:

```
 Usage: gal [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                        │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                 │
│ --help                        Show this message and exit.                                                                      │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ alarms             list or query alarms in the command centre                                                                  │
│ ch                 query or manage cardholders                                                                                 │
│ events             query command centre events                                                                                 │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

A simple example to get a list of cardholders looks like:

```
(gallagher-py3.11) ➜  gallagher git:(dto-implementation) ✗ gal ch list
                    Cardholders
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Id   ┃ First name  ┃ Last name     ┃ Authorised ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 8246 │ Johnetta    │ Abdallah      │ yes        │
│ 7936 │ Socorro     │ Abrahams      │ yes        │
│ 8374 │ Geoffrey    │ Acey          │ yes        │
│ 8370 │ Weldon      │ Acuff         │ yes        │
│ 7922 │ Rusty       │ Adelsperger   │ yes        │
```

you can also ask each sub command to give you in

## Resources

- [Command Line Interface Guidelines - clig.dev](https://clig.dev)