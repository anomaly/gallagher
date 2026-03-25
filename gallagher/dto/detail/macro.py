""" Macro Detail

"""

from typing import Optional

from ..utils import OptionalHrefMixin
from ..summary.macro import MacroSummary


class MacroDetail(MacroSummary):
    """Macro Detail

    A detailed view of a macro containing all information
    for comprehensive operations and management.
    """

    notes: Optional[str] = None
    trigger: OptionalHrefMixin = None
