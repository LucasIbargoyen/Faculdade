eletrodomestico = input("Qual eletrodoméstico você deseja ver o gasto: ")
watts = int(input("Quantos watts de potência tem esse eletrodoméstico?: "))
tempo = int(input("Quanto tempo o aparelho ficou ligado? "))

calculo_watts = (watts / 1000) * tempo

preco_uso = 0.7 * calculo_watts

print(f"O valor gasto de energia é de {calculo_watts}, o valor que você terá que pagar vai ser de {preco_uso:.2f}")
