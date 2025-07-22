
try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    divisao = numero1 / numero2
    print(f"A divisão de {numero1} por {numero2} é {divisao}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Por favor, insira apenas números inteiros.")
finally:
    print("Operação de divisão concluída.")