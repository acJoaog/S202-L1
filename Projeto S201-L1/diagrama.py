from abc import ABC,abstractmethod
import random

class Personagem():
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.inventario = []

    def atacar(self,personagem):
        dano = (self.danoAD + self.danoAP)*random.uniform(0, 2)
        personagem.vida -= dano
        print(f"{self.nome} deu {dano} em {personagem.nome}")

    def return_inv(self):
        lista = []
        for item in self.inventario:
            lista.append(item.nome)
        return lista

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = "Mago"
        self.danoAP = 600
        self.danoAD = 0
        self.vida = 2200

    def comprar(self, item):
        if self.saldo >= item.custo:
            self.saldo -= item.custo

            self.vida += item.vida
            self.danoAP += item.danoAP
            self.danoAD += item.danoAD

            self.inventario.append(item)
        else:
            print("saldo insuficiente")

class Tank(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = "Tank"
        self.danoAP = 0
        self.danoAD = 300
        self.vida = 4200

    def comprar(self, item):
        if self.saldo >= item.custo:
            self.saldo -= item.custo

            self.vida += item.vida
            self.danoAP += item.danoAP
            self.danoAD += item.danoAD

            self.inventario.append(item)
        else:
            print("saldo insuficiente")

class Assassino(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = "Assassino"
        self.danoAP = 300
        self.danoAD = 500
        self.vida = 2800

    def comprar(self, item):
        if self.saldo >= item.custo:
            self.saldo -= item.custo
            
            self.vida += item.vida
            self.danoAP += item.danoAP
            self.danoAD += item.danoAD

            self.inventario.append(item)
        else:
            print("saldo insuficiente")

class Item():
    def __init__(self, itemID, nome, vida, custo, danoAP, danoAD):
        self.itemID = itemID
        self.nome = nome
        self.vida = vida
        self.custo = custo
        self.danoAP = danoAP
        self.danoAD = danoAD

    
class Loja():
    def __init__(self, itens):
        self.itens = itens

    def mostrar_itens(self):
        print("mostrando itens")
        for item in self.itens:
            print(f"Id do item : {item.itemID} | Nome do Item: {item.nome} | custo: {item.custo} | danoAP: {item.danoAP} | danoAD: {item.danoAD}")
    
