# Odd and Even Lists
lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-' * 40)
print(f'Os números pares são: {lista[0]}')
print(f'Os números ímpares são: {lista[1]}')