class JogoDatabase:
    def __init__(self, database):
        self.db = database
    
    def create_player(self, nome, id):
        query = "create (:Player {nome: $nome, id: $id})"
        parameters = {"nome": nome, "id": id}
        self.db.execute_querry(query,parameters)

    def update_palyer(self, nome, id):
        query = "match (p:Player {id: $id}) set p.nome = $nome"
        parameters = {"id": id, "nome": nome}
        self.db.execute_querry(query,parameters)

    def get_players(self):
        query = "match (n:Player) return n.nome as nome"
        results = self.db.execute_querry(query)
        return [result["nome"] for result in results]
    
    def delete_player(self, id):
        query = "match (p:Player {id: $id})-[j:Join]-(m:Match) delete j,p"
        parameters = {"id": id}
        self.db.execute_querry(query,parameters)
    
    def create_match(self, id, Jogadores):
        query = "create (m:Match {id: $id})"
        parameters = {"id": id}
        self.db.execute_querry(query,parameters)

        for jogador in Jogadores:
            query = "match (m:Match {id: $idMatch}),(p:Player {id: $idPlayer}) create (p)-[:Join{score: $score}]->(m)"
            parameters = {"idMatch": id, "idPlayer": jogador['id'], "score": jogador['score']}
            self.db.execute_querry(query,parameters)
    
    def match_history(self,id):
        query = "match (p:Player {id: $id})-[j:Join]-(m:Match) return m.id as matchId, j.score as score"
        parameters = {"id": id}
        results = self.db.execute_querry(query,parameters)
        return [["matchId: {}, score: {}".format(result["matchId"], result["score"])] for result in results]

    def get_match(self, id):
        query = "match (p:Player)-[j:Join]-(m:Match {id: $id}) return p.nome as nome, j.score as score"
        parameters = {"id": id}
        results = self.db.execute_querry(query,parameters)
        return [["player: {}, score: {}".format(result["nome"], result["score"])] for result in results]