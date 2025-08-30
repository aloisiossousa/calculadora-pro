
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

def potencia(base, expoente):
        return base ** expoente


if __name__ == "__main__":


    while True:

        print("\n---Calculadora---")
        print("Digite 'sair' a qualquer momento para encerrar o programa")

        entrada_numero1 = input("Digite o primeiro numero: ")

        if entrada_numero1.lower() == "sair":
            break

        entrada_numero2 = input("Digite o segundo numero: ")

        if entrada_numero2.lower() == "sair":
            break

        try:
            num1_int = int(entrada_numero1)
            num2_int = int(entrada_numero2)

            soma = somar(num1_int, num2_int)
            multiplicacao = multiplicar(num1_int, num2_int)
            subtracao = subtrair(num1_int, num2_int)
            divisao = dividir(num1_int, num2_int)
            potenciacao = potencia(num1_int, num2_int)

            print(f"\n---RESULTADOS---")
            print(f"Somar: {soma}")
            print(f"Multiplicacao: {multiplicacao}")
            print(f"Subtracao: {subtracao}")
            print(f"Divisao: {divisao}")
            print(f"Potência: {potenciacao}")

        except ValueError:
            print("Erro: Por favor, digite apenas números inteiro")
            continue

print("Obrigado até a próxima")
