from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.cadastro_model import CadastroModel
from schemas.cadastro_schema import CadastroSchema
from core.deps import get_session
from datetime import datetime
from schemas.cadastro_schema import CadastroUpdateSchema
from fastapi import UploadFile, File
import csv
from io import StringIO

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CadastroSchema)
async def post_cadastro(cadastro: CadastroSchema, session: AsyncSession = Depends(get_session)):
    cadastro_data = cadastro.dict(exclude_unset=True)
    if cadastro_data.get('data_criacao') is None:
        cadastro_data['data_criacao'] = datetime.utcnow()
    if cadastro_data.get('data_atualizacao') is None:
        cadastro_data['data_atualizacao'] = datetime.utcnow()
    new_cadastro = CadastroModel(**cadastro_data)
    session.add(new_cadastro)
    await session.commit()
    await session.refresh(new_cadastro)
    return new_cadastro

@router.get("/", response_model=List[CadastroSchema])
async def get_cadastros(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CadastroModel))
    return result.scalars().all()

@router.get("/{cadastro_id}", response_model=CadastroSchema)
async def get_cadastro(cadastro_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CadastroModel).filter(CadastroModel.id == cadastro_id))
    cadastro = result.scalar()
    if cadastro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro not found")
    return cadastro

@router.put("/{cadastro_id}", response_model=CadastroSchema)
async def put_cadastro(cadastro_id: int, cadastro: CadastroUpdateSchema, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CadastroModel).filter(CadastroModel.id == cadastro_id))
    cadastro_db = result.scalar()
    if cadastro_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro not found")
    
    cadastro_data = cadastro.dict(exclude_unset=True)
    for key, value in cadastro_data.items():
        setattr(cadastro_db, key, value)
    
    cadastro_db.data_atualizacao = datetime.utcnow()  # Update the timestamp
    
    await session.commit()
    await session.refresh(cadastro_db)
    return cadastro_db

@router.delete("/{cadastro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cadastro(cadastro_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CadastroModel).filter(CadastroModel.id == cadastro_id))
    cadastro = result.scalar()
    if cadastro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cadastro not found")
    await session.delete(cadastro)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/import", status_code=status.HTTP_201_CREATED)
async def import_cadastros(file: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O arquivo deve ser um CSV")

    contents = await file.read()
    contents = contents.decode('utf-8')
    csv_data = StringIO(contents)

    reader = csv.DictReader(csv_data)
    cadastros = []
    for row in reader:
        cadastro = CadastroModel(
            nome=row['nome'],
            data_nascimento=row['data_nascimento'],
            genero=row['genero'],
            nacionalidade=row['nacionalidade'],
            data_criacao=datetime.utcnow(),
            data_atualizacao=datetime.utcnow()
        )
        cadastros.append(cadastro)

    session.add_all(cadastros)
    await session.commit()

    return {"cadastros_inseridos": len(cadastros)}