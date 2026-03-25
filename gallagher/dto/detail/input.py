""" Input Detail

"""

from typing import Optional

from ..summary.input import InputSummary


class InputDetail(InputSummary):
    """Input Detail

    A detailed view of an input containing all information
    for comprehensive operations and management.
    """

    input_type: Optional[str] = None
    notes: Optional[str] = None
    hardware_info: Optional[dict] = None
