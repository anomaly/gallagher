""" Decorators for annotating functions for behaviours.

    All decorators are defined here and are referenced across the codebase.
    Note that some of them reference the bootstrapped environment where
    information is discovered from the live Command Centre the instance
    is connected to.

    See Also:
        https://github.com/anomaly/gallagher/issues/69
"""

def deprecated(func):
    """Decorator to indicate that a function is deprecated.

    This decorator is used to indicate that a function is deprecated and
    should not be used. It will raise a warning when the function is called.

    Args:
        func (Callable): The function to be deprecated.

    Returns:
        Callable: The wrapped function.

    Examples:
        >>> @deprecated
        ... def old_function():
        ...     pass

    """
    import warnings
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(
            f"Call to deprecated function {func.__name__}.", 
            category=DeprecationWarning
        )
        return func(*args, **kwargs)

    return wrapper


def available(version_string):
    """Decorator to indicate that a function is available in a specific version.

    This decorator is used to indicate that a function is available in a specific
    version of the Command Centre API. It will raise an error if the function is
    called in a version that does not support it.

    Args:
        version_string (str): The version string the function is available in.

    Returns:
        Callable: The wrapped function.

    Examples:
        >>> @available("1.0.0")
        ... def new_function():
        ...     pass

    """
    import functools

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            from .cc.core import Capabilities

            if Capabilities.CURRENT.version < version_string:
                raise RuntimeError(
                    f"Function {func.__name__} is not available in version {Capabilities.CURRENT.version}."
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator