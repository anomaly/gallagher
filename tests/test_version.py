""" Tests to see that are running the tests against the right version
"""

from gallagher import __version__


async def test_version():
    assert __version__ == '0.1.0-alpha.3'
