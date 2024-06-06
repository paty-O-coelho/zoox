from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime

class CadastroModel(settings.DBBaseModel):
    __tablename__ = "cadastro"


    """
    nome	data_nascimento	genero	nacionalidade	data_criacao	data_atualizacao
    """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100))
    data_nascimento = Column(String)
    genero = Column(String(100))
    nacionalidade = Column(String(100))
    data_criacao = Column(DateTime)
    data_atualizacao = Column(DateTime)
