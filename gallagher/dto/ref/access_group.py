from ..utils import (
    AppBaseModel, 
    OptionalHrefMixin,
)


class AccessGroupRef(AppBaseModel, OptionalHrefMixin,):
    """Access Groups is what a user is assigned to to provide access to doors"""

    name: str
