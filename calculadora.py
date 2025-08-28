
def somar (num1, num2):
    resultado_soma = num1 + num2
    return resultado_soma

def multiplicar (num1, num2):
    resultado_multiplicacao = num1 * num2
    return resultado_multiplicacao

def subtrair (num1, num2):
    resultado_subtracao = num1 - num2
    return resultado_subtracao

def dividir (num1, num2):
    if num2 == 0:
        return "Erro: Divisão por Zero não é permitido"
    else: 
        resultado_divisao = num1 / num2
        return resultado_divisao


if __name__ == "__main__":
    print("Calculadora")


entrada_numero1 = input("Digite o primeiro numero: ")
entrada_numero2 = input("Digite o segundo numero: ")

try:
    num1_int = int(entrada_numero1)
    num2_int = int(entrada_numero2)

    soma = somar(num1_int, num2_int)
    multiplicacao = multiplicar(num1_int, num2_int)
    subtracao = subtrair(num1_int, num2_int)
    divisao = dividir(num1_int, num2_int)

    print(f"A somar é {soma}")
    print(f"A multiplicacao é {multiplicacao}")
    print(f"A subtracao é {subtracao}")
    print(f"A divisao é {divisao}")
except:
    print("Erro: Por favor, digite apenas números inteiro")
