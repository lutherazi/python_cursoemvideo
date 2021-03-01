# Tuple with soccer teams
print('{:=^40}'.format('Brasileirão'))
colocação = ('São Paulo', 'Internacional', 'Atlético MG', 'Flamengo', 'Palmeiras',
             'Grêmio', 'Fluminense', 'Santos', 'Corinthians', 'Atlético-PR',
             'Ceará SC', 'Bragantino', 'Atlético GO', 'Sport Recife', 'Vasco da Gama',
             'Fortaleza', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
print(f'A colocação do Brasileirão: {colocação}')
print('=' * 40)
print(f'Os 5 primeiros colocados: {colocação[0:5]}')
print('=' * 40)
print(f'Os 4 últimos colocados{colocação[-4:]}')
print('=' * 40)
print(f'Os times em ordem alfabética: {sorted(colocação)}')
print('=' * 40)
if 'Chapecoense' in colocação:
    print(f'O time Chapecoense se encontra na {colocação.index("Chapecoense") + 1}ª posição')
else:
    print('O time da Chapecoense não se encontra na primeira divisão do Brasileirão.')