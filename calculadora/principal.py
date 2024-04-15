print("✩ ✩ ✩ Calculadora ✩ ✩ ✩\n"
      "1 - Soma\n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão\n")

def soma():
    print("Soma\n")
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    print("Resultado: ", num1 + num2)

def subtracao():
    print("Subtração\n")
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    print("Resultado: ", num1 - num2)

def multiplicacao():
    print("Multiplicação\n")
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    print("Resultado: ", num1 * num2)

def divisao():
    print("Divisão\n")
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    print("Resultado: ", num1 / num2)

opcao = int(input("Escolha uma das opções: "))
if opcao == 1:
    soma()
elif opcao == 2:
    subtracao()
elif opcao == 3:
    multiplicacao()
elif opcao == 4:
    divisao()
else:
    print("Opção inválida")
    