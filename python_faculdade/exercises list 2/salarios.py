def ler_salarios():
    # Definindo os salários dos funcionários
    salarios = [1800, 2200, 1900, 2000, 800]
    print(
        f'Lista dos salários dos funcionários:\n'
        f'Funcionário 1: {salarios[0]}\n'
        f'Funcionário 2: {salarios[1]}\n'
        f'Funcionário 3: {salarios[2]}\n'
        f'Funcionário 4: {salarios[3]}\n'
        f'Funcionário 5: {salarios[4]}'
    )
    return salarios  # Retornando a lista de salários

def menor_salario(salarios):
    return min(salarios)  # Usando min() para encontrar o menor salário

def maior_salario(salarios):
    return max(salarios)  # Usando max() para encontrar o maior salário

def media(salarios):
    total = sum(salarios)  # Soma todos os salários
    average = total / len(salarios)  # Divide pelo número de salários
    return average

def salarios_soma(salarios):
    total = sum(salarios)
    return total

# Inicializando a variável salarios
salarios = []

while True:
    escolha = input("Digite o que você pretende fazer:\n Ver salários (V),\n Ver menor salário (M),\n Ver maior salário (N),\n ver a media (B),\n ver a soma (S),\n fechar sistema (P): \n").upper()

    if escolha == 'V':
        salarios = ler_salarios()  # Lê e retorna a lista de salários
    elif escolha == 'M':
        if salarios:  # Verifica se a lista de salários não está vazia
            menor = menor_salario(salarios)
            print(f'O menor salário é: {menor}')
        else:
            print('Por favor, verifique os salários primeiro.')
    elif escolha == 'N':
        if salarios:  # Verifica se a lista de salários não está vazia
            maior = maior_salario(salarios)
            print(f'O maior salário é: {maior}')
        else:
            print('Por favor, verifique os salários primeiro.')
    elif escolha == 'B':
        if salarios:  # Verifica se a lista de salários não está vazia
            media_salarios = media(salarios)  # Passa a lista de salários
            print(f'A média dos salários é: {media_salarios:.2f}')
        else:
            print('Por favor, verifique os salários primeiro.')
    elif escolha == 'S':
        if salarios:  # Verifica se a lista de salários não está vazia
            soma = salarios_soma(salarios)
            print(f'A soma dos salários é: {soma}')
        else:
            print('Por favor, verifique os salários primeiro.')
    elif escolha == 'P':
        print('Sistema fechado.')
        break
    else:
        print('Escolha Inválida')
