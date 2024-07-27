import http
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
import application.utilities.utils as utils

T = TypeVar("T")


class CamelBaseModel(BaseModel):
    class Config:
        alias_generator = utils.convert_str_to_camel
        arbitrary_types_allowed = True
        populate_by_name = True


class ResponseSchemaBase(CamelBaseModel):
    class Config:
        __abstract__ = True

    code: int = ""
    message: str = ""

    def success_response(self):
        self.code = http.HTTPStatus.OK
        self.message = 'Success'
        return self


class DataResponse(ResponseSchemaBase, Generic[T]):
    data: Optional[T] = None

    def success_response(self, data: Optional[T]):
        super().success_response()
        self.code = http.HTTPStatus.OK
        self.message = 'Success'
        self.data = data
        return self
