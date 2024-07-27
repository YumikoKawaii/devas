import http
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel
import application.utilities.utils as utils

T = TypeVar("T")


class CamelBaseModel(BaseModel):
    class Config:
        alias_generator = utils.convert_str_to_camel
        arbitrary_types_allowed = True
        populate_by_name = True


class ResponseSchemaBase(CamelBaseModel):
    __abtract__ = True

    code: int
    message: str

    def success_response(self):
        self.code = http.HTTPStatus.OK
        self.message = 'Success'
        return self


class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):

    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True

    def success_response(self, data: Optional[T]):
        self.code = http.HTTPStatus.OK
        self.message = 'Success'
        self.data = data
        return self
