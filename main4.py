from func import *

ln(30)
print("Use esse programa pra fazer uma saudação equivalente ao turno")
ln(30)

numeros = [1,2,3,4,5,6,7,8,90]
resultado = 0

def saudacao(hora):
    if (hora >= 0) and (hora < 6):
        resultado = f"Bom dia na madrugada"
    elif (hora >= 6) and (hora < 12):
        resultado = f"Bom dia!"
    elif (hora >= 12) and (hora < 18):
        resultado = f"Boa tarde"
    elif (hora >= 18) and (hora <= 23):
        resultado = f"Boa noite"
    else:
        resultado = f"Digite um número válido e inteiro para a hora"

    return resultado

entradaHora = int(input("Digite a hora da saudação: "))

ln(30)
print(saudacao(entradaHora))
ln(30)

