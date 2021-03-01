# Fibonacci Sequence v1.0
print('{:=^40}'.format(' Sequência Fibonacci! '))
n = int(input('Digite um número: '))
a = 0
b = 1
print('{0} -> {1} -> '.format(a, b), end='')
cont = 3 # 
while cont <= n:
    c = a + b
    print('{0} -> '.format(c), end='')
    a = b
    b = c
    cont += 1
print('Fim')
print('=' * 40)