

try:
    with open("arquivo_binario.bin", "w") as dados:
        dados.write("Python é incrível!")
    with open("arquivo_binario.bin", "r") as dados:
        print(dados.read())
except OSError:
    print("erro: algum problema no arquivo")