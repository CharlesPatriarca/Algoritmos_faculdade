def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 // num2


while True:

    print("SEJA BEM-VINDO(A) A CALCULADORA!")
    print()
    print("+-------------------+")
    print("| MENU DE OPERAÇÕES |")
    print("|  0 - sair         |")
    print("|  1 - somar        |")
    print("|  2 - subtrair     |")
    print("|  3 - multiplicar  |")
    print("|  4 - dividir      |")
    print("+-------------------+")

    escolha = int(input("Digite o número da operação que você deseja: "))

    print()

    if escolha == 0:
        print("Até a próxima")
        break

    if escolha == 1:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))

        print(f"O resultado da soma é: ", somar(n1, n2))

    elif escolha == 2:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))

        print(f"O resultado da subtração é: ", subtrair(n1, n2))

    elif escolha == 3:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))

        print(f"O resultado da multiplicação é: ", multiplicar(n1, n2))

    elif escolha == 4:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))

        print(f"O resultado da divisão é: ", dividir(n1, n2))

    else:
        print("Opção inválida. Digite novamente!")
