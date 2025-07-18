
nome = str(input('Digite seu nome: ')).strip()
idade = int(input("Digite sua idade:    "))

with open("Dados.txt", "a") as arquivo:
    print("arquivo Dados.txt aberto com sucesso!")
    arquivo.write(f"{nome} - {idade}")
