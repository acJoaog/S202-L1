class TeacherCRUD:
    def __init__(self, database):
        self.db = database
    
    def create_teacher(self, name, ano_nasc, cpf):
        query = "create (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_querry(query,parameters)

    def read_teacher(self,name):
        query = "match (t:Teacher{name: $name}) return t.name as nome, t.ano_nasc as ano, t.cpf as cpf;"
        parameters = {"name":name}
        results = self.db.execute_querry(query,parameters)
        print([["nome: {}, ano_nasc: {}, cpf: {}".format(result["nome"], result["ano"], result["cpf"])] for result in results])
    
    def delete_teacher(self, name):
        query = "match (t:Teacher {name: $name}) delete t;"
        parameters = {"name": name}
        self.db.execute_querry(query,parameters)

    def update_teacher(self, name, newCpf):
        query = "match (t:Teacher {name: $name}) set t.cpf = $newCpf;"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_querry(query,parameters)