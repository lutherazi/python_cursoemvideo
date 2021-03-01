# Dividing Values in Multiple Lists
lista = list()
par   = list()
impar = list()
while True:
    num =  int(input('Digite um número: '))
    lista.append(num)
    resp = input('Você deseja continuar? [Y/N] >> ')
    while resp not in 'YyNn':
        resp = input('Opção inválida! [Y/N] >> ')
    if resp in 'Nn':
        break
for key, value in enumerate(lista):
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
print('=-' * 30)
print(f'Os números na lista são: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são {impar}')