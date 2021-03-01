# Guessing Game v.1.0
import random

num = int(input('\nDigite um número de 0 a 5: '))
pc = random.randint(0, 5) #Sorteio do número
if num == pc:
    print('Você acertou! O número é: {}\n'.format(num))
else:
    print('Você errou! O número escolhido foi: {}\n'.format(pc))