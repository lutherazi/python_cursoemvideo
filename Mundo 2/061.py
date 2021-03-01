# Arithmetic progression v2.0
print('{:=^40}'.format(' Progressão Aritmética v2.0 '))
primeiro = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    print('{0} '.format(primeiro), end='-> ')
    primeiro += razao
    cont += 1
print('Acabou!')
print('=' * 40)