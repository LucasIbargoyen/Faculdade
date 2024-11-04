def base_to_decimal(number: str, base: int) -> int:
    # Verifica se a base está dentro do intervalo permitido
    if base < 2 or base > 36:
        raise ValueError("Base deve estar entre 2 e 36.")
    
    # Mapeia os caracteres para seus valores numéricos
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    decimal_value = 0
    number = number.upper()  # Para lidar com letras minúsculas

    for power, digit in enumerate(reversed(number)):
        if digit not in digits[:base]:
            raise ValueError(f"Digit '{digit}' is not valid for base {base}.")
        
        decimal_digit = digits.index(digit)  # Converte o dígito para seu valor
        decimal_value += decimal_digit * (base ** power)

    return decimal_value

def decimal_to_base(number: int, base: int) -> str:
    # Verifica se a base está dentro do intervalo permitido
    if base < 2 or base > 36:
        raise ValueError("Base deve ser entre 2 e 36")
    
    # Mapeia os valores numéricos para caracteres
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Trata o caso do número zero
    if number == 0:
        return "0"

    result = ""
    is_negative = number < 0
    number = abs(number)  # Trabalha com o valor absoluto

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result  # Adiciona o dígito correspondente
        number //= base  # Divide o número pela base

    # Adiciona sinal de negativo se o número original era negativo
    return '-' + result if is_negative else result

while True:
    escolha = input("Você quer converter de decimal para alguma base ou de uma base para decimal? 1 ou 2 ou 3 (para fechar o sistema): ")
    if escolha == '1':
        number = input("Digite o número que você quer converter para decimal: ")
        base = int(input("Digite a sua base: "))
        result = base_to_decimal(number, base)
        print(f"O número {number} na base {base} é igual a {result} em decimal.")
    elif escolha == '2':
        number = int(input("Digite o número decimal que você quer converter: "))
        base = int(input("Digite a base para qual você quer converter: "))
        result = decimal_to_base(number, base)
        print(f"O número {number} em decimal é igual a {result} na base {base}.")
    elif escolha == '3':
        print('Encerrando sistema.')
        break
    else:
        print("Escolha inválida!")
    

