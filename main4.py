from func import *

numeros = [1,2,3,4,5,6,7,8,90]

def soma(n1,n2):
    resultado = n1 + n2
    return resultado

acumulado = 0

for num in numeros:
    acumulado += num

print(acumulado)
