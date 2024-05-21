from ..utils import (
    AppBaseResponseModel,
    HrefMixin,
)

from ..summary import (
    AlarmSummary,
)


class AlarmSummaryResponse(
    AppBaseResponseModel,
):
    """AlarmSummaryResponse represents a single alarm"""

    alarms: list[AlarmSummary]
    updates: HrefMixin

    @property
    def cli_header(self):
        return ("id", "priority", "time", "type")

    def __rich_repr__(self):
        return (r.__rich_repr__() for r in self.alarms)

    def __str__(self):
        return f"{len(self.results)} cardholders"

