""" Exceptions declared by the Gallagher parser package

These are exceptions that extend standard Python exceptions to
indicate critical issues with configuration or parsing of
responses from the Gallagher API.

Everything declared here indicates an implementation error.
"""


class GCCBaseException(Exception):
    """Base exception for all Gallagher exceptions

    This is the base exception for all Gallagher exceptions.
    """


class UnlicensedFeatureException(GCCBaseException):
    """Raised when a feature is not licensed

    This exception is raised when the client attempts to access
    an endpoint that is not licensed by the server.

    """


class NotFoundException(GCCBaseException):
    """Raised if you tried to access an object that either does not
    exists or you don't have permission to access it.
    """


class ComingSoonException(GCCBaseException):
    """Raised if Gallagher has marked this feature to be coming soon

    These are items such as mutating a division which is scheduled
    but has not be released
    """


class DeadEndException(GCCBaseException):
    """Raised if an API the path is a dead end

    This is raised if the API path is not supported by the client
    these related to next, previous or updates that certain
    endpoints support.
    """


class AuthenticationError(GCCBaseException):
    """Error authentication against the CC API

    This is likely because the use has not provided an authentication
    key or is not allowed to access this resources with this
    particular key
    """


class PathFollowNotSupportedError(GCCBaseException):
    """Raised if the path is not supported by the client

    This is raised if the API path is not supported by the client
    these related to next, previous or updates that certain
    endpoints support.
    """
