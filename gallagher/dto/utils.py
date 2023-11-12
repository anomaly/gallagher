""" Data Transfer Object (DTO) utilities


"""


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

class IdentityMixin(BaseModel):
    """ Identifier 

    This mixin is used to define the identifier field for all
    responses from the Gallagher API.
    """
    id: str
    href: str

class HrefMixin(BaseModel):
    """ Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.
    """
    href: str
