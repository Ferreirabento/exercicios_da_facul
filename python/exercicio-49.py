
arquivo = str(input("Digite o nome do arquivo: "))
try:
    with open(arquivo, "r") as leitura:
        conteudo = leitura.read()
        print(f"Conteúdo do arquivo:{conteudo}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except IOError:
    print(f"Erro: Não foi possível ler o arquivo '{arquivo}'.")
else:
    print("Arquivo lido com sucesso!")
finally:
    print("Operação de leitura concluída.")

