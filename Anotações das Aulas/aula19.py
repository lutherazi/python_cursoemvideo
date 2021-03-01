estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for estado in brasil:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')
    print('---')
for v in estado.values():
    print(v, end='')
print()


'''
brasil  = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])
'''

'''
pessoas = {'nome': 'Gustavo',
           'sexo':'M',
           'idade':22
           }
pessoas['nome'] = 'Leandro'
for key, value in pessoas.items():
    print(f'{key.upper()} = {value}')

---------

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
'''