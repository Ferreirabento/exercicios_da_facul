
# LISTA DE LISTAS
dados = [
    [3, 5, 8],
    [10, 12, 15],
    [20, 25, 30]
]

# Procurar esse número
numero_procurado = 15
encontrado = False

# Seu código aqui
for lista in dados:
    for numero in lista:
        print(numero)
        if numero == numero_procurado:
            print(f"numero {numero_procurado} encontrado")
            encontrado = True
            break
    if encontrado:
        break