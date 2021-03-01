# Function for factorial
def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta. (Opcional).
    :return: O valor do Fatorial de um número Num.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Main Program
print(fatorial(5, True))
print(fatorial(5, False))
print(fatorial(8))
help(fatorial)
