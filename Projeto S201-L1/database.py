from typing import Collection
import pymongo
from dataset import dataset_itens


class Database:
    def __init__(self, database):
        self.connect(database)
        self.collection = None

    def connect(self, database):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db["itens"]
            self.collection.insert_many(dataset_itens)
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.db["personagens"])
            self.db.drop_collection(self.db["itens"])
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)