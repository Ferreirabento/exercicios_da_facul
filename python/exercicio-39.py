
animais = ["gato", "cachorro", "papagaio", "peixe", "coelho", "hamster"]

print(animais[0])
print(animais[-1])
animais[2] = "tartaruga"
print(animais[:3])
print(animais[::-1])
try:
    print(animais[10])
except IndexError:
    print("Error: indice não encontrado")
