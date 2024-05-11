""" Misc models

These are miscellaneous models that are used in places like alarms,
they may need to be refactored into other packages as we see fit. 
"""

from ..utils import (
    AppBaseModel,
    HrefMixin,
)


class InstructionRef(
    AppBaseModel,
    HrefMixin,
):
    """Operator reference

    At present used in Alarm details, revise as required.
    """

    name: str
