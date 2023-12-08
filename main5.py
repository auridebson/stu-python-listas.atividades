from func import *
from datetime import datetime

def soma(bate,volta):
    res = bate + volta
    return res


ln(30)
print("Digite dois números para fazer a soma")
ln(30)

entrada = soma(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")))


ln(10)
print(f"A soma dos dois números inseridos é: {entrada}")
ln(10)

print(f"A hora atual é {datetime.now().time()}")