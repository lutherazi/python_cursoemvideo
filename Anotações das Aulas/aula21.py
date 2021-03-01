# Interactive Help
help(input)

# -------------------------------
#docstrings
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)

# -------------------------------
# Argumento Opcionais
def somar(a=0, b=0, c=0):
    s = a + b+ c
    print(f'A soma vale {s}')


somar(3, 3, 5)
somar(3, 5)
somar(1)

# -------------------------------
# Escopo de variáveis
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}') # vai printar 4


n1 = 2
funcao()
print(f'N1 fora vale {n1}') # Vai printar 2

# -------------------------------
# Retorno de valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'A minha função tem o retorno de {r1}, {r2} e {r3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')