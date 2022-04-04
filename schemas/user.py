# Normal way
def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "nome":item["nome da categoria"],
        "produto":item["produto"],
        "preco":item["preço"],
        "marca":item["marca"],
        "decricao":item["descrição do produto"]
        
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]