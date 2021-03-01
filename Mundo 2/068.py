# Odd or Even Game!
from random import randint

cont = 0 # Victory Counter
print('{:=^40}'.format(' Par ou Ímpar! '))
while True:
    player = int(input('Digite um número: ')) # Player Choice
    pc = randint(0, 10) # Computer Choice
    soma = player + pc
    print('=' * 40)
    choice = ' '
    while choice not in 'PI':
        choice = input('[P] - PAR\n[I] - IMPAR\n>>> ').strip().upper()[0]
    print('Você escolheu {0} e o computador {1}. Total de {2}.'.format(player, pc, soma), end=' ')
    if soma % 2 == 0:
        print('Deu PAR!')
        if choice == 'P': # Player Choice == P
            cont += 1
            print('Parabéns, você GANHOU!')
            print('=' * 40)
        else:
            break
    else:
        print('Deu ÍMPAR!')
        if choice == 'I': # Player Choice == I
            cont += 1
            print('Parabéns, você GANHOU!')
            print('=' * 40)
        else:
            break
print('Você PERDEU! Você venceu um total de {0} vezes.'.format(cont))
print('{:=^40}'.format(' GAME OVER! '))