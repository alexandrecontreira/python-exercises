# 1- Crie um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

print('---------------------------------------------------')
print('------------ Olá seja bem-vindo -------------------')
print('---------------------------------------------------')

print("informe o valor ganho por hora: ")
valor_hora = float(input( ))
print("informe o número de horas trabalhadas: ")
num_hora = int(input( ))

sal_mes = valor_hora * num_hora

print((f'Seu salário deste mês é:{ round(sal_mes, 3) }').replace('.',','))
print( (f'seu salário deste mês é: R$ {sal_mes:.2f}').replace('.',','))

