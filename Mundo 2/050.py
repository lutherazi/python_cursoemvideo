# Arithmetic Progression
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        s = s + n #Usado para somar os valores
print('A soma dos números pares que você digitou foi: {0}'.format(s))