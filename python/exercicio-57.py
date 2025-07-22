
class ValorMuitoAltoError(Exception):
    pass

def sacar(valor):
    if valor > 1000:
        raise ValorMuitoAltoError("Valor muito alto para saque.")

try:
    valor = int(input("Digite o valor do saque: "))
    sacar(valor)
except ValueError:
    print("Valor inválido. Por favor, insira um número.")
except ValorMuitoAltoError:
    print("Erro: O valor do saque não pode ser maior que 1000.")
finally:
    print("Operação de saque finalizada.")
