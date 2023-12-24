""" Data Transfer Object (DTO) utilities


"""

from typing import (
    Optional
)
from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
)


def to_lower_camel(name: str) -> str:
    """
    Converts a snake_case string to lowerCamelCase
    """
    upper = "".join(word.capitalize() for word in name.split("_"))
    return upper[:1].lower() + upper[1:]


class AppBaseModel(BaseModel):
    """ Pydantic base model for applications

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
        alias_generator=to_lower_camel,
    )

    # Set to the last time each response was retrieved
    # If it's set to None then the response was either created
    # by the API client or it wasn't retrieved from the server
    #
    # This is generally used for caching
    good_known_since: Optional[datetime] = None

    # def model_post_init(self, __context) -> None:
    #     """
    #     The model_post_init method is called after the model is
    #     initialized, this is used to set the good_known_since

    #     https://docs.pydantic.dev/2.0/api/main/#pydantic.main.BaseModel.model_post_init
    #     """
    #     self.good_known_since = datetime.now()


class IdentityMixin(BaseModel):
    """ Identifier 

    This mixin is used to define the identifier field for all
    responses from the Gallagher API.
    """
    id: str


class HrefMixin(BaseModel):
    """ Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.
    """
    href: str


class OptionalHref(BaseModel):
    """ Optionally available Href

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
    href: Optional[str] = None
