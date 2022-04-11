from typing import Optional, Set
from pydantic import BaseModel

class Categoria(BaseModel):
    nome: str

class Produto(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    marca: Optional[str] = None
    categoria: Optional[Categoria] = None