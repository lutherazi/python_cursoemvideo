# Multiple Increases
#Salário > 1250 + 10% / Salário <= 1250 + 15%
sal = int(input('Digite o seu salário: R$'))
aum1 = (sal * 10 / 100) + sal
aum2 = (sal * 15 /100) + sal

if sal <= 1250:
    print('O novo salário será de: {0}'.format(aum2))
else:
    print('O novo salário será de: {0}'.format(aum1))