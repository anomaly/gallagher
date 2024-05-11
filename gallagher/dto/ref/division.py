from ..utils import AppBaseModel, IdentityMixin, HrefMixin


class DivisionRef(AppBaseModel, IdentityMixin, HrefMixin):
    """Division reference is used to link to a division

    The Mixins cover all the fields that are returned in the
    summary, hence nothing has to be declared in the body
    """

    pass
