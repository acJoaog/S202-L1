from bson.objectid import ObjectId
from diagrama2 import Mago,Tank,Assassino,Item

def convert_personagem(database, id):
    collection = database.db["personagens"]

    res = collection.find_one({"_id": ObjectId(id)})

    if res["classe"] == "Mago":
        return Mago(res["nome"])
    elif res["classe"] == "Tank":
        return Tank(res["nome"])
    elif res["classe"] == "Assassino":
        return Assassino(res["nome"])
    else:
        print("erro na conversao de classe")
        return None

def convert_itens(database):
    aux = []
    collection = database.db["itens"]

    res = collection.find()

    for item in res:
        x = Item(item["_id"],item["nome"],item["vida"],item["custo"],item["dano_AP"],item["dano_AD"])
        #print(x)
        aux.append(x)
    
    return aux

    