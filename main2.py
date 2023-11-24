from func import *

# Inverter Lista:

# Crie uma lista e escreva um programa para inverter a 
# ordem dos elementos da lista.

frutas_invertidas = []

for indice, fruta in enumerate(frutas) :
    print(f"{indice} - {fruta}")
ln(30)

while len(frutas) > 0:
    frutas_invertidas.append(frutas.pop())

for i, fr in enumerate(frutas_invertidas):
    print(f"{i} - {fr}")


