import math

def square(a):
    return math.pow(a, 2)

def sum():
    soma = int(input("Quantas vezes acumular: "))
    acumulado = 0
    for _ in range(soma):
       acumulado += square(5)
    return acumulado

print(sum())






