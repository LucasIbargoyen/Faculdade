real = float(input("Digite o valor em real: "))

dollar = float(input("Digite o valor do dolar atualmente: "))

calculo_real = real / dollar
calculo_taxa = calculo_real * (10/100)
taxa_aplicada = calculo_taxa + calculo_real

print(f"O valor da conversão de real para dolar é de {calculo_real:.2f}, com os 10% de taxa fica {taxa_aplicada:.2f}")