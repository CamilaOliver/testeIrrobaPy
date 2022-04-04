from typing import Optional, Set
from pydantic import BaseModel



class Categoria(BaseModel):
    nome: str

class Produto(BaseModel):
    produto: str
    descricao: Optional[str] = None
    preco: float
    marca: Set[str] = set()
    categoria: Optional[Categoria] = None