from ..utils import AppBaseModel, HrefMixin


class CompetencyRef(
    AppBaseModel,
    HrefMixin,
):
    """Reference to a Competency"""

    id: str
    name: str
