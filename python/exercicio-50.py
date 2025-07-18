
class MeuErro(Exception):
    pass

def cadastrar_usuario(nome, idade):
    try:
        if idade < 0 or idade > 130:
            raise MeuErro("IdadeInvalidaError: A idade deve estar entre 0 e 130 anos.")
        if not nome.isalpha():
            raise MeuErro("NomeInvalidoError: O nome deve conter apenas letras.")
    except MeuErro as erro:
        print(f"Erro: {erro}")
    else:
        print(f"Usuário {nome} cadastrado com sucesso! Idade: {idade} anos.")
    finally:
        print("Processo de cadastro finalizado.")

nome = str(input("Digite o nome do usuário: "))
idade = int(input("Digite a idade do usuário: "))
cadastrar_usuario(nome, idade)

