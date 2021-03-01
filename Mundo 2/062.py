# Arithmetic progression v3.0
print('{:=^40}'.format(' Progressão Aritmética v3.0 '))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont != total:
        print('{0} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('Fim')
    print('=' * 40)
    mais = int(input('Quantos termos você quer mostrar a mais?\n >>> '))
print('A PA possui {0} termos'.format(cont))
print('{:=^40}'.format(' Programa Finalizado '))