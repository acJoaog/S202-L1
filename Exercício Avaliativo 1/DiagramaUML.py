class Passageiro():
    def __init__(self, nome:str, documento:str) -> None:
        self.nome = nome
        self.documento = documento

class Corrida():
    def __init__(self, nota:int, distancia:float, valor:float, passageiro:Passageiro) -> None:
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista():
    def __init__(self, corridas, nota:int) -> None:
        self.corridas = corridas
        self.nota = nota
    

