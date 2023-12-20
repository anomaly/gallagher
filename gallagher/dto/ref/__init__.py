""" Reference classes

Our design outlines three types of DTO classes, Refs are ones that are
used to reference other objects, think of them as interlinks between
objects. They usually contain a href and some identifying information
such as a name or id.

This package was introduced in reference to this issue 
https://github.com/anomaly/gallagher/issues/21

which identified race conditions with circular imports. This is caused
mostly because of the nature of the data that the command centre exposes.
"""

from .access_group import (
    AccessGroupRef
)
