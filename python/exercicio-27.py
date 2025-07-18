
try:
    numero = int(input("Digite um número inteiro: "))
    print("Você digitou:", numero)
except ValueError:
    print("erro: Tipo digitado, por favor digite um numero inteiro")
