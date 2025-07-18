
try:
    with open("boas_vindas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("bem vindo ao python")

    with open("boas_vindas.txt", "r", encoding="utf-8") as arquivo:  #encoding="utf-8": para evitar problemas com acentuação
        print(arquivo.read())
except OSError:     #usar o OSError para evitar problemas com o arquivo (todo os problemas)
    print("erro: arquivo não encontrado")
