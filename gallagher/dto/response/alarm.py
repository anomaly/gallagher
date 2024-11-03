from ..utils import (
    AppBaseResponseModel,
    OptionalHrefMixin,
)

from ..summary import (
    AlarmSummary,
)


class AlarmSummaryResponse(
    AppBaseResponseModel,
):
    """AlarmSummaryResponse represents a single alarm"""

    alarms: list[AlarmSummary]
    updates: OptionalHrefMixin = None

    @property
    def result_set(self) -> list[AlarmSummary]:
        """ Wrap summary response target property

        the sql interface will call this property and each summary
        response is expected to override this and return the appropriate
        target property
        """
        return self.alarms

    @property
    def cli_header(self):
        return ("id", "priority", "time", "type")

    def __rich_repr__(self):
        return (r.__rich_repr__() for r in self.alarms)

    def __str__(self):
        return f"{len(self.results)} cardholders"


class AlarmUpdateResponse(
    AppBaseResponseModel,

):
    """Alarm updates for long poll

    updates: list[AlarmSummary]
    next: OptionalHrefMixin = None

    You should follow this response infinitely until the next
    href is None, this should update every 30 seconds or if
    there are changes to the alarms
    """
    updates: list[AlarmSummary]
    next: OptionalHrefMixin = None
