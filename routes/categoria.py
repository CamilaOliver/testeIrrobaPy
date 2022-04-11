from fastapi import APIRouter, Query, HTTPException
from models.model import Categoria
from config.db import conn 
from schemas.model import serializeDict, serializeList
from bson import ObjectId
categoria = APIRouter() 

@categoria.get('/categorias')
async def find_all_categorias():
    return serializeList(conn.local.categoria.find())

@categoria.post('/categorias')
async def create_categoria(categoria: Categoria):
    conn.local.categoria.insert_one(dict(categoria))
    return HTTPException(status_code=200, detail="Categoria inserida")

@categoria.put('/categorias/{id}')
async def update_categoria(id,categoria: Categoria):
    if (len(id) < 24):
        return HTTPException(status_code=422, detail="ID incorreto")
    else:
        if (conn.local.categoria.find_one(ObjectId(id))):
            conn.local.categoria.find_one_and_update({"_id":ObjectId(id)},{
                "$set":dict(categoria)
            })
            return serializeDict(conn.local.categoria.find_one({"_id":ObjectId(id)}))
        else:
            return HTTPException(status_code=404, detail="Catogoria não encontrada")

@categoria.delete('/categorias/{id}')
async def delete_categoria(id: str = Query(..., min_length=24)):
    if (len(id) < 24):
        return HTTPException(status_code=422, detail="ID incorreto")
    else:
        if (conn.local.categoria.find_one(ObjectId(id))):
            return serializeDict(conn.local.categoria.find_one_and_delete({"_id":ObjectId(id)}))
        else:
            return HTTPException(status_code=404, detail="Catogoria não encontrada")