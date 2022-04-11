from fastapi import FastAPI
from routes.categoria import categoria
from routes.produto import produto 
app = FastAPI()
app.include_router(categoria)
app.include_router(produto)


@app.get("/")
def index():
    return {"title": "Teste Py Irroba:)"}
