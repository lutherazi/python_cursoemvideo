# Draw and sum functions
from random import randint
from time   import sleep

# Draw
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

# Sum
def somaPar(lista):
    soma = 0
    for s in lista:
        if s % 2 == 0:
            soma += s
    print(f'Somando os valores pares de {lista}, temos {soma}!')


# Main Program
números = list() 
sorteia(números)
somaPar(números)