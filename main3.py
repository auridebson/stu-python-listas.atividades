from func import *


# PEDIR AO USUÁRIO: NOME, IDADE, ALTURA, SALÁRIO
# GUARDE AS INFORMAÇÕES EM UM DICIONÁRIO
# CHECAR:
# - SE MAIOR QUE 18 MOSTRE MENSAGEM NA TELA
# - SE SALÁRIO < QUE 1500 MOSTRE MENSAGEM NA TELA
# - SE SALÁRIO < 1500
# - SE SALÁRIO FOR < 3000 E > 1500
# - SE SALÁRIO FOR < 5000 E > 3000
# - SE SALÁRIO FOR > 5000

bd = {
    "id": 1,
    "nome": "auridebson",
    "idade": 46,
    "altura": 1.81,
    "salario": 100000,
}


ln(30)
print("Inclusão de dados de usuário no sistema")
ln(30)

entrada = input

# Listar dados do dicinário
# for dado in bd:
#     print(bd[dado])