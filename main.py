# 1 - Soma de Listas:
# Crie duas listas numéricas e escreva um programa para calcular 
# a soma de elementos correspondentes nas duas listas.

def ln(x):
    print("-"*x)

lista1 = [46,42,24,22]
lista2 = [42,38,41,41]
i = 0

ln(30)
for numero in lista1:
    print(f"{lista1[i]} + {lista2[i]} = {lista1[i]+lista2[i]}")
    i = i+1
ln(30)