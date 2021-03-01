# Soccer Player Registration
dict = {}
list = []
print(f'{" CADASTRO DE JOGADOR ":=^40}')
dict['Nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dict["Nome"]} jogou? '))
for c in range(0, partidas):
    dict['Gols'] = list
    list.append(int(input(f'Quantos gols na partida {c + 1}? ')))
print(f'{" JOGADOR ":=^40}')
print(f'O jogador {dict["Nome"]} jogou {partidas} partidas.')
for k, v in enumerate(dict['Gols']):
    print(f'-> Na partida {k + 1}, {dict["Nome"]} fez {v} gols.')
print(f'Foi um total de {sum(list)} gols!')