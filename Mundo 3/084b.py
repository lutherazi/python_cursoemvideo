# Composite list and Data Analysis
princ = []
temp  = []
maior = menor = 0
print(f'{" CADASTRO DE PESSOAS ":-^80}')
while True:
    temp.append(input('Nome: '))              #   --> key [0]
    temp.append(float(input('Peso: ')))       #   --> key [1]
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])                   #   --> Transfere os elementos para a lista principal
    temp.clear()                            #   --> Limpa a lista temporário
    resp = input('Você deseja continuar? [Y/N] >> ')
    if resp in 'Nn':
        break
print('-' * 40)
print(f'Foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso é {maior}Kg, sendo as pessoas com esse peso: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso é {menor}Kg, sendo as pessoas com esse peso: ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
print('-' * 40)