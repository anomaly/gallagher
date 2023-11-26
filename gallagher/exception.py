""" Exceptions declared by the Gallagher parser package

These are exceptions that extend standard Python exceptions to
indicate critical issues with configuration or parsing of
responses from the Gallagher API.

Everything declared here indicates an implementation error.
"""


class UnlicensedFeatureException(Exception):
    """ Raised when a feature is not licensed

    This exception is raised when the client attempts to access
    an endpoint that is not licensed by the server.

    """
    pass
