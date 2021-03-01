# Extracting data from a list
lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    choice = input('Deseja digitar mais algum valor? [Y/N] >> ').upper().strip()
    while choice not in 'YN':
        choice = input('Digite uma opção válida [Y/N] >> ').upper().strip()
    if choice in 'N':
        break
lista.sort(reverse = True)
print(f'Foi digitado {len(lista)} números.')
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print(f'Se o número 5 está na lista, ele está na posição {lista.count(5)}.')
else:
    print(f'O número 5 não está na lista...')