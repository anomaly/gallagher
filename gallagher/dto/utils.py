""" Data Transfer Object (DTO) utilities

These are utilities that DTO refs, summaries and detail objects
inherit from. It defines the basic parsing mechanism based on the
configuration of each endpoint class.

In addition we provide a based class for Responses to encapsulate
behaviour outlined by the Gallagher API.

Mixins are classes that provided an isolated behaviour for DTO
classes to inherit from, for example Identifier, Hrefs, etc.

There are some utility functions that are used internally, please
ignore them unless you are developing the client itself.

"""

from typing import (
    Optional,
)
from functools import cached_property
from typing_extensions import Annotated

from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    HttpUrl,
    Field,
)

# Annotations for fields that are reserved words in Python
from_optional_datetime = Annotated[
    Optional[datetime],
    Field(..., alias="from")
]

until_optional_datetime = Annotated[
    Optional[datetime],
    Field(..., alias="until")
]


# Helper functions for parsing
def _to_lower_camel(name: str) -> str:
    """Converts a snake_case string to lowerCamelCase

    Not designed for use outside of the scope of this package
    """
    upper = "".join(word.capitalize() for word in name.split("_"))
    return upper[:1].lower() + upper[1:]


# Ensure that the primitive wrappers such as Mixins appear
# before the generic classes for parsing utilities


class IdentityMixin(BaseModel):
    """Identifier

    This mixin is used to define the identifier field for all
    responses from the Gallagher API.
    """

    id: str


class HrefMixin(BaseModel):
    """Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.
    """

    href: HttpUrl

class TypeValuePair(BaseModel):
    """Type Value Pair

    This class is used to represent a type value pair in the
    Gallagher system. It is used in many places to represent
    a key value pair.

    eg this appears in CardholderDetail:

    {
        "type": "active",
        "value": "Active"
    }

    """

    type: str
    value: str

class OptionalHrefMixin(BaseModel):
    """Optionally available Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.

    Primarily used by the discovery endpoint, where the href
    may be absent if the feature is not available.

    Reason for this so the API Endpoint configuration can
    reference the href property (pre discovery), otherwise
    the Feature* classes have a None object for the object

    # Use with caution

    Only use these with responses that don't optionally
    require a href. See Gallagher's documentation for
    confirmation.
    """

    href: Optional[HttpUrl] = None


class AppBaseModel(BaseModel):
    """Pydantic base model for applications

    This class is used to define the base model for all schema
    that we use in the Application, it configures pydantic to
    translate between camcelCase and snake_case for the JSON
    amongst other default settings.

    ORM mode will allow pydantic to translate SQLAlchemy results
    into serializable models.

    For a full set of options, see:
    https://pydantic-docs.helpmanual.io/usage/model_config/
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=_to_lower_camel,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    @classmethod
    def _accumulated_annotations(cls) -> dict:
        """Return a dictionary of all annotations

        This method is used to return a dictionary of all the
        annotations from itself and it's parent classes.

        It is intended for use by the shillelagh extension
        """
        annotations = cls.__annotations__.copy() # TODO: should we  make copies?
        for base in cls.__bases__:
            if issubclass(base, BaseModel):
                # Copy annotations from classes that are pydantic models
                # they are the only things that form part of the response
                annotations.update(base.__annotations__)
        return annotations.items()

    # Set to the last time each response was retrieved
    # If it's set to None then the response was either created
    # by the API client or it wasn't retrieved from the server
    #
    # This is generally used for caching
    _good_known_since: Optional[datetime] = None

    def model_post_init(self, __context) -> None:
        """
        The model_post_init method is called after the model is
        initialized, this is used to set the _good_known_since

        https://docs.pydantic.dev/2.0/api/main/#pydantic.main.BaseModel.model_post_init
        """
        self._good_known_since = datetime.now()

    def __repr__(self) -> str:
        """Return a string representation of the model

        This method is used to return the string representation of the
        model, it's used for debugging purposes.

        https://docs.python.org/3/reference/datamodel.html
        """
        return f"{self.__class__.__name__}({self.model_dump()})"


class AppBaseResponseModel(AppBaseModel):
    """Response Model

    Response classes should subclass this not AppBaseModel, so that
    the framework can differentiate between Model classes and responses.

    AppBaseResponseWithFollowModel sub classes from this, and adds
    functionality for following next, updates or going back to the previous
    set of results.

    """

    pass


class AppBaseResponseWithFollowModel(AppBaseResponseModel):
    """Response with optional Follow links

    Many responses from the Gallagher system return next, previous and update
    links. This is typical when there are a large number of responses
    where the absence of a next link denotes that the client has fetched
    all pending objects.

    Some endpoints return an `update` URL which can be followed to poll
    for responses.


    """

    next: OptionalHrefMixin = None  # None means it's the end of responses
    previous: OptionalHrefMixin = None  # None means first set of responses
    updates: OptionalHrefMixin = None  # None means no updates to watch for
