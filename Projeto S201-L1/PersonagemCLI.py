from diagrama2 import Mago,Tank,Assassino

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def remove_command(self, name):
        if name in self.commands:
            del self.commands[name]
            print(f"Comando '{name}' removido, não é possivel criar mais personagens.")
        else:
            print(f"Command '{name}' not found.")

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


class personagemCLI(SimpleCLI):
    def __init__(self, personagemDAO):
        super().__init__()
        self.personagemDAO = personagemDAO
        self.add_command("create", self.create_personagem)
        self.add_command("read", self.read_personagem)
        self.add_command("update", self.update_personagem)
        self.add_command("delete", self.delete_personagem)

    def create_personagem(self):
        classe = input("Escolha a Classe: Mago,Tank,Assassino: ")
        while True:
            if classe == "Mago":
                personagem = Mago(input("nome do personagem: "))
                self.remove_command("create")
                break
            elif classe == "Tank":
                personagem = Tank(input("nome do personagem: "))
                self.remove_command("create")
                break
            elif classe == "Assassino":
                personagem = Assassino(input("nome do personagem: "))
                self.remove_command("create")
                break
            else:
                print("Classe invalida")  
            classe = input("Escolha a Classe: Mago,Tank,Assassino")
        
        self.personagemDAO.create_personagem(personagem)

    def read_personagem(self):
        try:
            id = input("Enter the id: ")
            personagem = self.personagemDAO.read_personagem(id)
            if personagem:
                print(f"Nome do Personagem: {personagem['nome']} | DanoAP: {personagem['danoAP']} | DanoAD: {personagem['danoAD']} | Vida: {personagem['vida']} | Saldo: {personagem['saldo']}  | Inventario: {personagem['inventario']}")
        except:
            pass

    def update_personagem(self):
        id = input("Entre com o id do personagem para edita-lo: ")
        self.personagemDAO.update_personagem(id)

    def delete_personagem(self):
        id = input("Entre com o id do personagem para exclui-lo: ")
        self.personagemDAO.delete_personagem(id)
        
    def run(self):
        print("Bem vindo a criação de personagem!")
        print("Comando disponiveis: create, read, update, delete, quit")
        super().run()