
mais_dados = input("Digite mais dados: ")

with open("Dados.txt", "a") as arquivo:
    arquivo.write(f"\n{mais_dados}\n")
