# Multiplication Table v2.0
print('{:=^40}'.format('TABUADA AUTOMÁTICA'))
num = int(input('Digite um número: '))
print('=' * 40)
for c in range(1, 11):
    print('{0} x {1:2} = {2}'.format(num, c, num * c))
print('=' * 40)