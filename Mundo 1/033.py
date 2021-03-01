# Highest and lowest values
n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
p1 = n1 > n2 > n3
p2 = n1 > n3 > n2
p3 = n2 > n1 > n3
p4 = n2 > n3 > n1
p5 = n3 > n2 > n1
p6 = n3 > n1 > n2
if p1:
    print('O maior é {0} e o menor é {1}\n'.format(n1, n3))
if p2:
    print('O maior é {0} e o menor é {1}\n'.format(n1, n2))
if p3:
    print('O mairo é {0} e o menor é {1}\n'.format(n2, n3))
if p4:
    print('O maior é {0} e o menor é {1}\n'.format(n2, n1))
if p5:
    print('O maior é {0} e o menor é {1}\n'.format(n3, n1))
if p6:
    print('O maior é {0} e o menor é {1}\n'.format(n3, n2))