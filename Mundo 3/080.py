# Sorted list with no repetitions
lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    for key, value in enumerate(lista):
        if num < value:
            lista.insert(key, num)
            print(f'O número {num} foi adicionado na posição {key} da lista.')
            break
    else:
        lista.append(num)
        print(f'O número {num} foi adicionado no final da lista.')
print(f'A lista ordenada sem sort fica: {lista}')