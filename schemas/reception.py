from typing import Literal

from pydantic import BaseModel


class ReceptionResponse(BaseModel):
    intent: Literal["GENERAL", "EDIT"]
    message: str