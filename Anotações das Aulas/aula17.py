num = [2, 5, 9, 1] # Lista normal
print(num)

num[2] = 3 # Alterando um valor na lista
print(num)

num.append(7) # Adicionando um valor no final da lista
print(num)

num.sort() # Deixando em ordem a lista
print(num)

num.sort(reverse=True) # Deixando em ordem contrária
print(num)

print(f'Essa lista tem {len(num)} elementos.') # Contagem dos elementos da lista

num.insert(2, 0) # Insere um elemento a partir da ordem que você quer
print(num)

num.pop(2) # Deleter o valor indicado na posição
print(num)

num.insert(2, int(input('Digite um número: '))) # Adicionar um novo valor
print(num)

for v in num:
    print(f'{v} ', end='')

for c, v in enumerate(num):
    print(f'Na posição {c + 1} encontrei o valor {v}!')
print('Fim')

valores = list() # Criar uma lista
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
b = a # Ligação entre variaveis
c = a[:] # Copia entre variaveis
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')