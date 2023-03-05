"""
"""

from .utils import AppBaseModel, IdentityMixin

class API(
    AppBaseModel
):

    features: List[str]