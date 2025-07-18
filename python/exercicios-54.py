import csv

dados = [
    ["Produto", "Preço"],
    ["Arroz", "20"],
    ["Feijão", "10"],
    ["Macarrão", "8"]
]


with open("produtos.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
    
with open("produtos.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(f"\n{linha[0]} custa R$ {linha[1]}\n")
 

