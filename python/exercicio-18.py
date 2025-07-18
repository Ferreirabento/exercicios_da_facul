

def calcular_media(lista):
    media = float(0)
    soma = int(0)
    for nota in lista:
        soma += nota
    media = soma // len(lista)
    return media

notas = [7.0, 8.5, 6.0]
media = calcular_media(notas)
print("Média final:", media)

