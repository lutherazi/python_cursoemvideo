# Predictions for the Mega Sena
from random import randint

palpites  = []
print(f'{" MEGA SENA ":-^40}')
jogos = int(input('Quantos jogos você deseja jogar? '))
print('-' * 40)
for palp in range(0, jogos):
    while len(palpites) != 6:
        num  = randint(0, 60)
        if num not in palpites:
            palpites.append(num)
    palpites.sort()
    for lista in palpites:      # Formatting Predictions
        print((f'{lista:^2} - '), end='')
    print('Boa sorte!')
    print('-' * 40)
    if len(palpites) == 6:
        palpites = []
print()