# Leap Year
ano = int(input('\nDigite o ano: '))
pri = ano % 4
seg = ano % 400
ter = ano % 4
quar = ano % 100
if pri != 0 and seg != 0:
    print('O ano {0} não é um ano bissexto.\n'.format(ano))

if ter == 0 and quar != 0:
    print('O ano {0} é bissexto\n'.format(ano))