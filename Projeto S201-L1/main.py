from database import Database
#from writeAJson import writeAJson
from PersonagemDAO import PersonagemDAO
from PersonagemCLI import personagemCLI
from util import convert_personagem, convert_itens
from diagrama import Loja
from bson.objectid import ObjectId
import random

try:
    db = Database(database="Projeto")

    # Instanciando os itens do Banco de Dados para Classe Loja
    loja = Loja(convert_itens(db))

    # Criando Personagem 1
    personagem1 = PersonagemDAO(db)
    print("Criando personagem 1")
    cliPersonagem1 = personagemCLI(personagem1)
    cliPersonagem1.run()

    # Criando Personagem 2
    personagem2 = PersonagemDAO(db)
    print("Criando personagem 2")
    cliPersonagem2 = personagemCLI(personagem2)
    cliPersonagem2.run()

    # instanciando informações do banco de dados para objetos de classes
    p1 = convert_personagem(db, personagem1.id)
    p2 = convert_personagem(db, personagem2.id)

    # Realização dos Turnos
    rodada = 1
    while ( p1.vida > 0 and p2.vida > 0):
        print(f"- Inciando rodada {rodada} -")
        rodada += 1

        # Realizando ataques dos personagens
        p1.atacar(p2)
        p2.atacar(p1)

        # Distribuindo Gold para os personagens
        g1 = random.randint(120, 300) #gold personagem 1
        p1.saldo += g1
        print(f"{p1.nome} ganhou {g1} de ouro.")

        g2 = random.randint(120, 300) #gold personagem 1
        p2.saldo += g2
        print(f"{p2.nome} ganhou {g2} de ouro.")

        print("Deseja visitar a Loja ? S/N")
        msg = input()
        if msg == "S":
            print("Bem vindo a Loja. \nComandos disponíveis: listar, comprar, sair.")
            aux = input()
            while(aux != "sair"):
                if aux == "listar":
                    print(f"saldo do p1 = {p1.saldo}, saldo do p2 = {p2.saldo}")
                    loja.mostrar_itens()
                    
                elif aux == "comprar":
                    try:
                        p = input("Deseja comprar itens para o personagem 1 ou 2 ?")
                        if p == "1":
                            i = input("Insira o id do Item desejado.")
                            for item in loja.itens:
                                if str(item.itemID) == i:
                                    p1.comprar(item)
                        elif p == "2":
                            i = input("Insira o id do Item desejado.")
                            for item in loja.itens:
                                if str(item.itemID) == i:
                                    p2.comprar(item)
                        else:
                            print("erro - personagem inválido!")
                    
                    except Exception as e:
                        print(e)
                print("Comandos disponíveis: listar, comprar, sair.")
                aux = input()

    
    print("- Fim de jogo -")

    if p1.vida > 0:
        print(f"{p1.nome} é o vencedor(a)!")
    
    if p2.vida > 0: 
        print(f"{p2.nome} é o vencedor(a)!")

    if p1.vida <= 0 and p2.vida <= 0:
        print(f"Houve um empate!")


except Exception as e:
    print(e)
finally:
    collection = db.db["personagens"]

    # Guardando personagem 1 no BD
    collection.update_one({"_id": ObjectId(personagem1.id)}, {"$set":{
                "nome": p1.nome,
                "classe": p1.classe,
                "dano_AP": p1.danoAP,
                "dano_AD": p1.danoAD,
                "vida": p1.vida,
                "saldo": p1.saldo,
                "inventario": p1.return_inv()
                }
            })
    
    # Guardando personagem 2 no BD
    collection.update_one({"_id": ObjectId(personagem2.id)}, {"$set":{
                "nome": p2.nome,
                "classe": p2.classe,
                "dano_AP": p2.danoAP,
                "dano_AD": p2.danoAD,
                "vida": p2.vida,
                "saldo": p2.saldo,
                "inventario": p2.return_inv()
                }
            })
    
    # Agregation Pipeline para retornar a média de saldo final da partida

    # Calcular a média do campo "dano_saldo"
    resultado = collection.aggregate([
        {"$group": {"_id": None, "media_dano_saldo": {"$avg": "$saldo"}}}
    ])
    # Extrair o resultado
    for documento in resultado:
        media_saldo = documento["media_dano_saldo"]
        print(f"A média do saldo final da partida é: {media_saldo}")

    