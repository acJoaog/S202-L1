class Personagem():
    def __init__(self, nome, vida, danoAP, danoAD, saldo):
        self.nome = nome
        self.danoAP = danoAP
        self.danoAD = danoAD
        self.vida = vida
        self.saldo = saldo
        self.inventario = []

    def atacar(self,personagem):
        personagem.setVida -= (self.danoAP + self.danoAD)

    def comprar(self, item):
        if self.saldo >= item.custo:
            saldo -= item.custo
            self.inventario.append(item)
        else:
            print("saldo insuficiente")

class Item():
    def __init__(self, itemID, nome, custo, danoAP=0, danoAD=0):
        self.itemID = itemID
        self.nome = nome
        self.custo = custo
        self.danoAP = danoAP
        self.danoAD = danoAD
    
class Loja():
    def __init__(self, itens):
        self.itens = itens

    def mostrar_itens(self):
        for item in self.itens:
            print(f"Id do item : {item.itemID} | Nome do Item: {item.nome} | custo: {item.custo} | danoAP: {item.danoAP} | danoAD: {item.danoAD}")