from ..utils import AppBaseModel, HrefMixin


class AccessGroupRef(AppBaseModel, HrefMixin):
    """Access Groups is what a user is assigned to to provide access to doors"""

    name: str
