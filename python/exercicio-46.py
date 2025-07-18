
import csv

alunos = [["nome", "idade"], ["joão", "20"]]

try:
    with open("alunos.csv", "w", newline="", encoding="utf-8") as dados: #evita linhas em branco no windows
        informacoes = csv.writer(dados)
        informacoes.writerows(alunos)

    with open("alunos.csv", "r", encoding="utf-8") as dados:
        print(dados.read())
except OSError:
    print("erro: algum problema no arquivo")


