
try:
    lista = [1, 2, 3, 4]
    print("Último item:", lista[4])
except:
    print("erro: indice inexistente")
    print("correção...")
    lista = [1, 2, 3, 4]
    print("Último item:", lista[3])