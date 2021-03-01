# Python Dictionary
ficha = dict()
print(f'{" Ficha do Aluno ":=^40}')
ficha['Nome']  = input('Nome: ')
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado!'
elif 5 <= ficha['Média']:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado!'
print('-' * 40)
for k, v in ficha.items():
    print(f'-> {k}: {v}')
print(f'{" Volte Sempre! ":=^40}')