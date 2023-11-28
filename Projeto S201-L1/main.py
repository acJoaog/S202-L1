from database import Database
#from writeAJson import writeAJson
from PersonagemDAO import PersonagemDAO
from PersonagemCLI import personagemCLI
from util import convert_personagem, convert_itens
from diagrama2 import Loja

try:
    db = Database(database="Projeto")

    #personagem1 = PersonagemDAO(db)
    #print("Criando personagem 1")
    #cliPersonagem1 = personagemCLI(personagem1)
    #cliPersonagem1.run()

    #personagem2 = PersonagemDAO(db)
    #print("Criando personagem 2")
    #cliPersonagem2 = personagemCLI(personagem2)
    #cliPersonagem2.run()

    # instanciando informações do banco de dados para objetos de classes
    #p1 = convert_personagem(db, personagem1.return_id)
    #p2 = convert_personagem(db, personagem2.return_id)

    loja = Loja(convert_itens(db))
    loja.mostrar_itens()

except Exception as e:
    print(e)
finally:
    db.resetDatabase()