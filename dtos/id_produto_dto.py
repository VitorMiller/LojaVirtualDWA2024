from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *


class IdProdutoDTO(BaseModel):
    id_produto: int


    @field_validator("id_produto")
    def validar_id(cls, v):
        msg = is_greater_than(v, "Id do Produto", 0)
        if msg:
            raise ValueError(msg)
        return v


  