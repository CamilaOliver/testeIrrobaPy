from fastapi import APIRouter, HTTPException, Query
from models.model import Produto
from config.db import conn 
from schemas.model import serializeDict, serializeList
from bson import ObjectId
produto = APIRouter() 

@produto.get('/produtos')
async def find_all_produtos():
    return serializeList(conn.local.produto.find())

@produto.post('/produtos')
async def create_produto(produto: Produto):
    conn.local.produto.insert_one(dict(produto))
    return HTTPException(status_code=200, detail="Produto inserido")

@produto.put('/produtos/{id}')
async def update_produto(id,produto: Produto):
    if (len(id) < 24):
        return HTTPException(status_code=422, detail="ID incorreto")
    else:
        if (conn.local.produto.find_one(ObjectId(id))):
            conn.local.produto.find_one_and_update({"_id":ObjectId(id)},{
                "$set":dict(produto)
            })
            return serializeDict(conn.local.produto.find_one({"_id":ObjectId(id)}))
        else:
            return HTTPException(status_code=404, detail="Produto não encontrado")
            
@produto.delete('/produtos/{id}')
async def delete_produto(id: str = Query(..., min_length=24)):
    if (len(id) < 24):
        return HTTPException(status_code=422, detail="ID incorreto")
    else:
        if (conn.local.produto.find_one(ObjectId(id))):
            return serializeDict(conn.local.produto.find_one_and_delete({"_id":ObjectId(id)}))
        else:
            return HTTPException(status_code=404, detail="Produto não encontrado")
  