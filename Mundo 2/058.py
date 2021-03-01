#Guessing Game v2.0
import random

print('{:=^50}'.format(' Jogo de adivinhação '))
print(('Acabei de pensar em um número entre 0 e 10...\nVocê consegue acertar?'))
print('-' * 50)
pc = random.randint(0, 10)
tentativas = 0  # Retry Counter
while True:
    n = int(input('Qual o seu palpite?\n>>> '))
    tentativas = tentativas + 1
    if n == pc:
        break
    else:
        if n < pc:
            print('Mais...')
        elif n > pc:
            print('Menos...')
print('{:=^50}'.format(' VOCÊ GANHOU! '))
print('Parabéns, você acertou com {0} tentativas!\nEu tinha pensando no número {1}.'.format(tentativas, pc))
print('{:=^50}'.format(' GAME OVER! '))