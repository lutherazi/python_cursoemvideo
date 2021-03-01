# Uniting dictionaries and lists
ficha = {}
lista = list()
cont = soma = media = 0
print(f'{" CADASTRO ":=^40}')
while True:
    ficha['Nome']  = input('Nome: ')
    while True:
        ficha['Sexo']  = input('Sexo [M/F]: ')
        if ficha['Sexo'] in 'mf':
            break
    ficha['Idade'] = int(input('Idade: '))
    cont += 1; soma += ficha['Idade']; media = soma / cont
    escolha = input('Deseja continuar? [S/N] >> ')
    lista.append(ficha.copy())
    print('-' * 40)
    if escolha in 'Nn':
        break
print(f'A) Foram cadastradas {cont} pessoas.')
print(f'B) As mulheres cadastradas foram: ', end='')
for i in lista:
    if i['Sexo'] == 'f':
        print(i['Nome'], end=' -> ')
print('Fim!')
print(f'C) A média da idade é {media:.2f}')
print(f'D) As pessoas mais velhas que a média são: ', end='')
for i in lista:
    if i['Idade'] > media:
        print(i['Nome'], end=' -> ')
print('Fim!')
print(f'{" PROGRAMA FINALIZADO ":=^40}')