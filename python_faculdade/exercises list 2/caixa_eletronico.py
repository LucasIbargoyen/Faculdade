saldo = 2000
decisao = input("O que você deseja fazer? para sacar (S), para depositar (D), para verificar saldo (A): ")

def saque (saldo):
    ordem = int(input("Digite quanto você quer sacar: "))
    saldo -= ordem
    return saldo

def deposito(saldo):
    ordem = int(input("Digite o valor que você quer depositar: "))
    saldo += ordem
    return saldo

def verificar_saldo(saldo):
    return saldo

if decisao == 'S':
    saldo = saque(saldo)
    print(f'Saldo após o saque: {saldo}')

elif decisao == 'D':
    saldo = deposito(saldo)
    print(f'Saldo depois o depósito: {saldo}')

elif decisao == 'A':
    saldo = verificar_saldo(saldo)
    print(f'Seu saldo é de: {saldo}')