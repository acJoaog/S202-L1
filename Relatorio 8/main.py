from database import Database
from jogo_database import JogoDatabase

db = Database("bolt://3.239.236.150:7687","neo4j","chairwomen-duplicate-wash")
db.drop_all()

game = JogoDatabase(db)

game.create_player("Joao","player1")
game.create_player("Pedro","player2")
game.create_player("Lucas","player3")
game.create_player("Matheus","player4")

game.create_match  ("Match 1",[{"id":"player1","score":600},{"id":"player3","score":350},{"id":"player4","score":100}])
game.create_match  ("Match 2",[{"id":"player2","score":800},{"id":"player4","score":400}])
game.create_match  ("Match 3",[{"id":"player1","score":750},{"id":"player2","score":900},{"id":"player3","score":300}])

game.update_palyer("Joao Gabriel","player1")
game.update_palyer("Pedro Augusto","player2")

game.delete_player("player3")

game.get_players()

print(game.get_match("Match 2"))

print(game.match_history("player1"))
print(game.match_history("player4"))

