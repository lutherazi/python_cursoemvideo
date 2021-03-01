# Analyze data in a tuple
num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')))
print(f'\nOs números digitados foram {num}.')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('Não foi encontrado o número 3.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')