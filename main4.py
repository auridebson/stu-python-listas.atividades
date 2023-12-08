from func import *

nomes = ["auridebson", "luciana", "levy", "guilherme"]

def saudacao(nome1, nome2):
    if  nome1 in nomes:
        print("Poxa! Você está olhando para um cara lindo!")
        print("------")
    print(f'Olá, você está olhando para {nome1} mas quem está ao seu lado é {nome2}')


ln(30)
saudacao("luciana","Maria")
ln(30)