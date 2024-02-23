# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .dataset_part import DatasetPart
from .dataset_type import DatasetType
from .dataset_validation_status import DatasetValidationStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Dataset(pydantic.BaseModel):
    id: str = pydantic.Field(description="The dataset ID")
    name: str = pydantic.Field(description="The name of the dataset")
    created_at: dt.datetime = pydantic.Field(description="The creation date")
    updated_at: dt.datetime = pydantic.Field(description="The last update date")
    dataset_type: DatasetType
    validation_status: DatasetValidationStatus
    validation_error: typing.Optional[str] = pydantic.Field(default=None, description="Errors found during validation")
    schema_: typing.Optional[str] = pydantic.Field(
        alias="schema", default=None, description="the avro schema of the dataset"
    )
    required_fields: typing.Optional[typing.List[str]] = None
    preserve_fields: typing.Optional[typing.List[str]] = None
    dataset_parts: typing.Optional[typing.List[DatasetPart]] = pydantic.Field(
        default=None, description="the underlying files that make up the dataset"
    )
    validation_warnings: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, description="warnings found during validation"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}