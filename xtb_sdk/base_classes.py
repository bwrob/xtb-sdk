"""
Base classes for all XTB data models
"""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class DataModel(BaseModel):
    """
    Base class for all XTB data models.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
        use_enum_values=True,
    )

    def dict(self, **kwargs) -> dict:
        """Override dict to include aliasing"""
        return self.model_dump(by_alias=True, **kwargs)
