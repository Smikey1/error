from typing import Any

from pydantic import BaseModel


class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Any | None


def success(data, message="Successful") -> ResponseModel:
    return ResponseModel(**{"success": True, "message": message, "data": data})


def failure(message="Something went wrong") -> ResponseModel:
    return ResponseModel(**{"success": False, "message": message})
