
def desconto(valor, porcentagem):
    desconto = (porcentagem / 100) * valor
    valor_com_desconto = valor - desconto
    return valor_com_desconto

print(desconto(valor=200, porcentagem=25))
