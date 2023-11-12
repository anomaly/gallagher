"""

"""

from .utils import (
    AppBaseModel,
    HrefMixin
)

class FeatureAccessGroups(
    AppBaseModel,
):
    access_groups: HrefMixin

class APIFeatures(
    AppBaseModel,
):
    access_groups: FeatureAccessGroups

class API(
    AppBaseModel,
):
    """
    The API obje
    """

    version: str
    features: APIFeatures

    @property
    def get_sem_ver(self):
        """ Get a SemVer tuple from the version string
        """
        return self.version.split(".")
