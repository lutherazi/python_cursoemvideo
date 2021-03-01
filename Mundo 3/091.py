# Python Dice Game
from random import randint
from time   import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print(f'{" COMPETIÇÃO DE DADOS ":=^40}')
for k, v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{" RANKING ":=^40}')
for k, v in enumerate(ranking):
    print(f'{k + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
print(f'{" VOLTE SEMPRE! ":=^40}')