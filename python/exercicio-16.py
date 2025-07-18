
try:
    numero_a = int(input("digite um numero: "))
    numero_b = int(input("digite outro numero: "))
    print(numero_a / numero_b)
    print(numero_a // numero_b)
    print(numero_a % numero_b)
except ZeroDivisionError:
    print("não é peritido dividir por zero")
