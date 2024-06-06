from typing import Optional
from pydantic import BaseModel as SCBaseModel
from datetime import datetime

class CadastroSchema(SCBaseModel):
    id: Optional[int] = None
    nome: Optional[str]
    data_nascimento: Optional[str]
    genero: Optional[str]
    nacionalidade: Optional[str]
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    class Config:
        orm_mode = True


class CadastroUpdateSchema(SCBaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[str] = None
    genero: Optional[str] = None
    nacionalidade: Optional[str] = None

    class Config:
        orm_mode = True