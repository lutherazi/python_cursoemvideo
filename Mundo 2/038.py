# Comparing numbers
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('{0} é maior que {1}.'.format(n1, n2))
elif n2 > n1:
    print('{0} é maior que {1}.'.format(n2, n1))
else:
    print('{0} é igual a {1}.'.format(n1, n2))