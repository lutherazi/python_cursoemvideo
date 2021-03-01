# Factorial Calculation
print('{:=^50}'.format(' CALC. FATORIAL '))
num = int(input('Digite um número para calcular a sua Fatorial: '))
c = num
f = 1
print('Calculando fatorial: !{0} = '.format(num), end='')
while c > 0:
    print('{0}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c #f = f * c
    c -= 1 #c = c - 1
print('{0}'.format(f))
print('=' * 50)