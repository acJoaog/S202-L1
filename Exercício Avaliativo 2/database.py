from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password) -> None:
        self.driver = GraphDatabase.driver(uri,auth=(user,password))

    def close(self):
        self.driver.close()

    def execute_querry(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
        
    def drop_all(self):
        with self.driver.session() as session:
            session.run("match (n) detach delete n")