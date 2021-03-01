# Highest and lowest values in tuple
from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'''\nO maior número é: {max(num)}
O menor número é: {min(num)}''')