from pymongo import MongoClient
from bson.objectid import ObjectId
from DiagramaUML import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista:Motorista):
        try:

            res = self.db.collection.insert_one({"nota":motorista.nota})

            i = 0
            for corrida in motorista.corridas:
                nova_corrida = {
                    "Corrida "+ str(i) :{
                    "nota":corrida.nota,
                    "distancia":corrida.distancia,
                    "valor":corrida.valor,
                    "passageiro":{
                        "nome":corrida.passageiro.nome,
                        "documento":corrida.passageiro.documento
                    }
                    }
                }
                self.db.collection.update_one({"_id":res.inserted_id}, {"$set":nova_corrida})
                i += 1

            print(f"motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"motorista found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, nota:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota":nota}})
            print(f"motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None