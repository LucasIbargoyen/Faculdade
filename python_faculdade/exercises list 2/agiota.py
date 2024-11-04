#JUROS: 1.5%

devendo = 1000

def saldo_devedor_atual(tempo):
    juros = (1000 * 0.015) * tempo
    divida = devendo + juros
    return divida


def mes_seguinte(tempo):
    juros = (1000 * 0.015) * tempo
    prox_mes = devendo + juros
    return prox_mes

while True:
    escolha = input("Você quer ver a situação da divida atual ou ver a próxima parcela?\n Digite A para ver a atual ou S para ver a do próximo mês:\n ").upper()
    if escolha == 'A':
        divida = saldo_devedor_atual(10)
        print(f'O saldo da dívida atual é de: {divida}')
    elif escolha == 'S':
        divida = mes_seguinte(11)
        print(f'O saldo futuro da dívida no mês seguinte é de: {divida}')
    else:
        print("Escolha inválida")

