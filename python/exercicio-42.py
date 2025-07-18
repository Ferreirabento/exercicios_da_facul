
# MATRIZ DADA
matriz = [
    [11, 4, 7],
    [6, 9, 2],
    [8, 5, 10]
]

# Seu código aqui
for lista in matriz:
    for numero in lista:
        if numero % 2 != 0:
            continue
        print(numero)
