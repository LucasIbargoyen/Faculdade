def ler_opcao():
    print("Escolha uma das opções:")
    print("S - Sacar")
    print("D - Depositar")
    print("A - Verificar saldo")
    opcao = input("Digite a opção desejada: ").upper() 
    return opcao


def apresentar_quantidade(saldo):
    print(f"O saldo atual é: {saldo}")


def saque(saldo):
    valor = int(input("Digite quanto você quer sacar: "))
    saldo -= valor
    return saldo


def deposito(saldo):
    valor = int(input("Digite o valor que você quer depositar: "))
    saldo += valor
    return saldo


saldo = 2000


opcao = ler_opcao()

if opcao == 'S':
    saldo = saque(saldo)
    print(f"Saldo após saque: {saldo}")
elif opcao == 'D':
    saldo = deposito(saldo)
    print(f"Saldo após depósito: {saldo}")
elif opcao == 'A':
    apresentar_quantidade(saldo)
else:
    print("Opção inválida.")