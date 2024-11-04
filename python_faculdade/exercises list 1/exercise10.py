import math

triangul_retangulo = int(input("Qual é a medida do triangulo retangulo? "))
cateto_adjacente = int(input("Digite o valor do cateto adjacente: "))
cateto_oposto = int(input("Digite o valor do cateto oposto: "))

hipotenusa = math.sqrt((cateto_adjacente ** 2) + (cateto_oposto ** 2))

print(f"O valor da hipotenusa é de {hipotenusa} mm")
