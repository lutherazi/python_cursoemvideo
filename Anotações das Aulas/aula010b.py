n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segudna nota: '))
s = (n1 + n2) / 2
print('\nA sua média é: {0:.1f}'.format(s))
if s >= 6:
    print('Aprovado!\n')
else:
    print('Reprovado!\n')