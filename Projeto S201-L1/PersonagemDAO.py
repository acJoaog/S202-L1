from pymongo import MongoClient
from bson.objectid import ObjectId
from diagrama import Personagem


class PersonagemDAO:
    def __init__(self, database):
        self.id = None
        self.collection = database.db["personagens"]

    def create_personagem(self, personagem):
        
        try:
            
            res = self.collection.insert_one({
                "nome": personagem.nome,
                "classe": personagem.classe,
                "dano_AP": personagem.danoAP,
                "dano_AD": personagem.danoAD,
                "vida": personagem.vida,
                "saldo": 0
            })
            
            print(f"classe criada com o id: {res.inserted_id}")
            self.id = res.inserted_id
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating personagem: {e}")
            return None

    def read_personagem(self, id: str):
        try:
            res = self.collection.find_one({"_id": ObjectId(id)})
            print(f"personagem: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading personagem: {e}")
            return None

    def update_personagem(self, id: str):
        try:
            res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {
                "nome": input("nome do personagem: ")
            }})
            print(f"personagem updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating personagem: {e}")
            return None

    def delete_personagem(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"personagem deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting personagem: {e}")
            return None
    
    def return_id(self):
        return self.id
    