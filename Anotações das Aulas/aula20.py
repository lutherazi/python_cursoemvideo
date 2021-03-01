# CRIANDO UMA FUNÇÃO
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)

# USANDO FOR
def contador(* núm):
    for valor in núm:
        print(f'Valor: {núm} ', end='')
    print('Fim!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# USANDO len
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e ssão ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# DESEMPACOTAMENTO
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)


# LISTA - MAS TÁ ERRADO 
valores = []

def dobra(* lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# PROGRAMA PRINCIPAL
while True:
    valores.append(input('Digite um número: '))
    escolha = str(input('Deseja continuar? S/N'))
    if escolha in 'n':
        break
print(valores)
dobra(valores)
print(valores)