
aluno = {"nome": "joão", "idade": 20, "curso": "ADS", "nota final": 9.5}
print(f"o nome é {aluno['nome']} com a nota: {aluno['nota final']}")
aluno["aprovado"] = True
aluno["nota final"] = 9.0
del aluno["idade"]
print(aluno)
