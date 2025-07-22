import os

arquivo = str(input("Digite o nome do arquivo: "))
if os.path.exists(arquivo):
    try:
        with open(arquivo, "r") as file:
            conteudo = file.read()
            print(f"conteudo do aquivo {arquivo} é\n{conteudo}")
    except OSError as e:
        print(f"Erro ao ler o arquivo: {e}")
else:
    print(f"arquivo {arquivo} não existe.")

