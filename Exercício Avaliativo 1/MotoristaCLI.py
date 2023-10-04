from DiagramaUML import *
from writeAJson import writeAJson

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class motoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        
        corridas = []
        
        print("Cadastrando corridas")
        flag = True
        while flag:
            nomePassageiro = input("Entre com o nome do passageiro: ")
            documentoPassageiro = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nomePassageiro,documentoPassageiro)
            nota = int(input("Insira a nota da corrida: "))
            distancia = float(input("Insira a distancia: "))
            valor = float(input("Insira o valor: "))
            corrida = Corrida(nota,distancia,valor,passageiro)
            corridas.append(corrida)

            escolha = input("digite sair para terminar crição de corridas: ")
            if escolha == "sair":
                flag = False

        nota = 0
        for corrida in corridas:
            nota += corrida.nota
    
        motorista = Motorista(corridas,nota/len(corridas))
        self.motoristaDAO.create_motorista(motorista)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motoristaDAO.read_motorista(id)
        if motorista:
            print(f"nota: {motorista['nota']}")

    def update_motorista(self):
        nota = input("Entre com a nova nota: ")
        self.motoristaDAO.update_motorista(id, nota)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motoristaDAO.delete_motorista(id)
        
    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
