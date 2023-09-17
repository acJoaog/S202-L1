from database import Database
from writeAJson import writeAJson
from livrosModel import livrosModel
from cli import LivroCLI

db = Database(database="Relatorio_05", collection="livros")
livros = livrosModel(database=db)

personCLI = LivroCLI(livros)
personCLI.run()
