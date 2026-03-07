""" Output Detail

"""

from typing import Optional

from ..summary.output import OutputSummary


class OutputDetail(OutputSummary):
    """Output Detail

    A detailed view of an output containing all information
    for comprehensive operations and management.
    """

    output_type: Optional[str] = None
    notes: Optional[str] = None
    hardware_info: Optional[dict] = None
