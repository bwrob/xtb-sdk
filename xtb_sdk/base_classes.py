from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class XtbModel(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    def __call__(self) -> dict:
        return self.model_dump(by_alias=True)