# Composite list and Data Analysis
cadastro = []
dados    = []
maior_peso = menor_peso = 0
while True:
    dados.append(input('Nome: '))               # --> key = 0
    dados.append(int(input('Peso: ')))          # --> key = 1
    if len(cadastro) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    resp = input('Deseja cadastrar outra pessoa? [Y/N] >> ')
    if resp in 'Nn':
        break
print(f'Os dados são: {cadastro}')
print(f'Foram cadastradas {len(cadastro)}')
print(f'Maior peso: {maior_peso}Kg, sendo as pessoas com esse peso: ', end='')
for pessoas in cadastro:
    if pessoas[1] == maior_peso:
        print(f'{pessoas[0]}', end=' ')
print()
print(f'Menor peso: {menor_peso}Kg, sendo as pessoas com esse peso: ', end='')
for pessoas in cadastro:
    if pessoas[1] == menor_peso:
        print(f'{pessoas[0]}', end=' ')
print()
print('Fim!')