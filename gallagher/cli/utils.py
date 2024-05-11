""" Asyncio patches for Typer

There's a thread open on the typer repo about this:
    https://github.com/tiangolo/typer/issues/88

Essentially, Typer doesn't support async functions. This is an issue
post migration to async, @csheppard points out that there's a work
around using a decorator on the click repository:
https://github.com/tiangolo/typer/issues/88#issuecomment-612687289

@gilcu2 posted a similar solution on the typer repo:
https://github.com/tiangolo/typer/issues/88#issuecomment-1732469681

this particular one uses asyncer to run the async function in a thread
we're going in with this with the hope that the official solution is
closer to this than a decorator per command.
"""

import inspect

from functools import (
    partial,
    wraps,
)

import asyncer
from typer import Typer


class AsyncTyper(Typer):
    @staticmethod
    def maybe_run_async(decorator, f):
        if inspect.iscoroutinefunction(f):

            @wraps(f)
            def runner(*args, **kwargs):
                return asyncer.runnify(f)(*args, **kwargs)

            decorator(runner)
        else:
            decorator(f)
        return f

    def callback(self, *args, **kwargs):
        decorator = super().callback(*args, **kwargs)
        return partial(self.maybe_run_async, decorator)

    def command(self, *args, **kwargs):
        decorator = super().command(*args, **kwargs)
        return partial(self.maybe_run_async, decorator)
