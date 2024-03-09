from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class XtbModel(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
        use_enum_values=True,
    )

    def dict(self, **kwargs) -> dict:
        return self.model_dump(by_alias=True, **kwargs)
