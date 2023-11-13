from database import Database

db = Database("bolt://52.3.235.203:7687","neo4j","terminations-runaway-dollar")

#Questão 1
print("Questão 1")

#A)
print("A)")
results = db.execute_querry("match (t:Teacher{name:'Renzo'}) return t.ano_nasc as ano, t.cpf as cpf;")
for result in results:
    print("Ano_nasc: "+ str(result["ano"]))
    print("cpf: "+ str(result["cpf"]))

#B)
print("B)")
results = db.execute_querry("match (t:Teacher) where t.name starts with 'M' return t.ano_nasc as ano, t.cpf as cpf;")
for result in results:
    print("Ano_nasc: "+ str(result["ano"]))
    print("cpf: "+ str(result["cpf"]))

#C)
print("C)")
results = db.execute_querry("match (c:City) return c.name as nome;")
print("Nome das cidades:")
for result in results:
    print(str(result["nome"]))

#D)
print("D)")
results = db.execute_querry("match (s:School) where s.number >= 150 and s.number <= 500 return s.name as nome, s.address as end, s.number as num;")
for result in results:
    print("Nome da Escola: "+ str(result["nome"]))
    print("Endereço: "+ str(result["end"]))
    print("Número: "+ str(result["num"]))

#Questão 2
print("\nQuestão 2")

#A)
print("A)")
results = db.execute_querry("match (t:Teacher) return min(t.ano_nasc) as ano1, max(t.ano_nasc) as ano2;")
for result in results:
    print("Ano_nasc: "+ str(result["ano1"]))
    print("Ano_nasc: "+ str(result["ano2"]))

#B)
print("B)")
results = db.execute_querry("match (c:City) return avg(c.population) as avg")
for result in results:
    print("Population avg: "+ str(result["avg"]))

#C)
print("C)")
results = db.execute_querry("match (c:City{cep:'37540-000'}) return replace(c.name, 'a', 'A') as nome;")
for result in results:
    print("Nome alterado: "+ str(result["nome"]))

#D)
print("D)")
results = db.execute_querry("match (t:Teacher) return substring(t.name, 3, 1) as terceira_letra;")
for result in results:
    print("Caractere do professor: "+ str(result["terceira_letra"]))