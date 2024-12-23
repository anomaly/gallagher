from typing import (
    Annotated,
)

from ..utils import (
    AppBaseResponseModel,
)

from ..detail import (
    FeaturesDetail,
    VersionsDetail,
)


class DiscoveryResponse(
    AppBaseResponseModel,
):
    """A response that outlines the capability of the server

    Gallagher requires customers to license individual features, if they are
    the server will return a 403 HTTP code. The purpose of this model is to
    discover what features are available on the server.

    The response should be memoized as it is unlikely to change during individual
    sessions, they can however change over a period of time.

    This API client is updated to work with various versions of the server, the
    server responds with a version string that can be used to determine if
    the API client can work with the server.
    """

    version: Annotated[str, "The version of the server"] = "0.0.0.0"
    versions: Annotated[
        VersionsDetail, 
        "A list of versions available on the server"
    ] = VersionsDetail()
    features: Annotated[
        FeaturesDetail, "A list of features available on the server"
    ] = FeaturesDetail()

    @property
    async def get_sem_ver(self):
        """Get a SemVer tuple from the version string"""
        return self.version.split(".")
