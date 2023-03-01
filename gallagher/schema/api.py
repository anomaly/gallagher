"""
"""

from .utils import AppBaseModel, IdentityMixin

class AccessGroup(
    AppBaseModel
):
    pass
    

class Features(
    AppBaseModel
):
    access_groups: AccessGroup

class API(
    AppBaseModel
):

    features: List[str]