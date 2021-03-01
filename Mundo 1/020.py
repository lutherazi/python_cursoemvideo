# Drawing an order from the list
from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
#sorteio = ('{0}, {1}, {2}, {3}'.format(a1, a2, a3,a4).split())
sorteio = [a1, a2, a3, a4]
shuffle(sorteio) #Lembrar de que quando você importar toda a biblioteca, usar o nome dela antes.
print('Resultado: {0}'.format(sorteio))