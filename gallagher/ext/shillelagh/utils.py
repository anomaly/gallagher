


@classmethod
def _shillelagh_columns(cls) -> dict:
    """Return the model as a __shillelagh__ compatible attribute config

    Rules here are that we translate as many dictionary vars into
    a __shillelagh__ compatible format.

    If they are hrefs to other children then we select the id field for
    each one of those objects
    """
    from shillelagh.fields import (
        Field,
        Integer,
        String,
        Boolean,
        Blob,
        Collection,
        Date,
        DateTime,
        Float,
        ISODate,
        ISODateTime,
        IntBoolean,
        StringBlob,
        StringBoolean,
        StringDate,
        StringDateTime,
        StringDecimal,
        StringDuration,
        StringInteger,
        StringTime,
    )

    _map = {
        int: Integer,
        str: String,
        bool: Boolean,
        bytes: Blob,
        list: Collection,
        datetime: DateTime,
        float: Float,
    }

    # Make a key, value pair of all the class attributes
    # that are have a primitive type
    table_fields = {
        key: _map[value]()
        for key, value in cls.__annotations__.items() # annotations not fields
        if not key.startswith("_") and value in _map
    }
    return table_fields