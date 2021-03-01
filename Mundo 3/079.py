# Unique values in a list
lista = list()
while True:  
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'O número {lista[-1]} foi adicionado.')
    else:
        print(f'O número {num} já foi adicionado na lista e não será duplicado.')

    r = input('Você deseja continuar? [Y/N] >> ')       
    while r not in 'YyNn':
        r = input('Digite uma opção válida! [Y/N] >> ')
    if r in 'Nn':
        break
lista.sort()
print(f'Os números digitados foram: ', end='')
for c in lista:
    print(f'{c} ', end='')