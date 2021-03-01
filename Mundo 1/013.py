# Salary readjustment
sal = float(input('Atual salário: R$'))
aum = sal * 15 / 100
new_sal = sal + aum
print('-' * 12)
print('O salário de R${0:.2f}, recebeu um aumento de R${1:.2f}, sendo o novo salário: R${2:.2f}'.format(sal, aum, new_sal))
print('-' * 12)