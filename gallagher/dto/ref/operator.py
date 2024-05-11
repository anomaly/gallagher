""" Operator

An operator is someone who has operated an door and caused an
event like an alarm.

"""

from ..utils import (
    AppBaseModel,
)


class OperatorRef(
    AppBaseModel,
):
    """Operator reference

    At present used in Alarm details, revsie as required.
    """

    name: str
