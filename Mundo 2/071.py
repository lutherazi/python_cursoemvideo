# ATM Simulator
from random import rand

print('{:=^40}'.format(' Banco Azi '))
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print('Total de {0} cédulas de R${1}'.format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('Fim')