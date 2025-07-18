
tupla = ("ricardo", "29", "maranhão", ["futbol", "cerveja", "pagode"])
print(tupla[2])
nome, idade, cidade, hobies = tupla
print(nome)
print(idade)
print(cidade)
print(hobies)
try:
    tupla[2] = 30
except:
    print("erro: não é possivel mudar as informaçoes na tupla")
tupla[3][0] = "tenis"
print(tupla) #é possivel mudar porque eu estou mundando o lista detro da tupla deixando ela intacta 