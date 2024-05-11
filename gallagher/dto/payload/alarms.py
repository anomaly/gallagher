from ..utils import (
    AppBaseModel,
)


class AlarmCommentPayload(AppBaseModel):
    """Comment Payload

    This is the payload used to create a comment on an object.
    """

    comment: str
