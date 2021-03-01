# Highest and lowest values in the list
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}ª: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Foi digitado os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for key, value in enumerate(lista):
    if value == maior:
        print(f'{key}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for key, value in enumerate(lista):
    if value == menor:
        print(f'{key}... ', end='')