
try:
    numero1 = int(input("digite um numero inteiro: "))
    numero2 = int(input("digite o proximo: "))
    divisao = numero1 / numero2
except ValueError:
    print("erro: por favor digite um numero inteiro")
except ZeroDivisionError:
    print("erro: não é possivel dividir por zero")
else:
    print(f"a divisao entre {numero1} e {numero2} é {divisao}")
finally:
    print("-----fim do programa-----")
