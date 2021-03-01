#AULA DE MÓDULO IMPORTANDO APENAS ALGO ESPECÍFICO DA BIBLIOTECA
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número é: {0}, sendo ele arredondado para cima: {1}'.format(raiz, floor(raiz)))
print('A raiz do número é: {0}, sendo ele arredondado para baixo: {1}'.format(raiz, ceil(raiz)))