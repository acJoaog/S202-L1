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

class teacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD):
        super().__init__()
        self.teacherCRUD = teacherCRUD
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        self.teacherCRUD.create_teacher(str(input("name: ")), input("ano_nasc: "), str(input("cpf: ")))

    def read_teacher(self):
        self.teacherCRUD.read_teacher(str(input("Nome do Professor: ")))

    def update_teacher(self):
        self.teacherCRUD.update_teacher(str(input("Insira o nome do professor que deseja alterar: ")), str(input("Insira o novo CPF: ")))

    def delete_teacher(self):
        self.teacherCRUD.delete_teacher(str(input("Insira o nome do Professor a ser Deletado: ")))
        
    def run(self):
        print("Welcome to the teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
