from typing import Collection
import pymongo # pip install pymongo
from dataset import dataset_classes, dataset_itens


class Database:
    def __init__(self, database):
        self.connect(database)

    def connect(self, database):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.db.get_collection["classes"].insert_many(dataset_classes)
            self.db.get_collection["itens"].insert_many(dataset_itens)
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            #self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)