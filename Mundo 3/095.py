# Enhancing Dictionaries
jogador  = {}
partidas = []
time     = []
print(f'{" CADASTRO DE JOGADOR ":=^40}')
# -> Filling the dictionary
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c + 1}ª partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        escolha = input('Deseja continuar? [Y/N] >> ')
        if escolha in 'NnYy':
            break
        print('Erro! Digite uma opção válida.')
    if escolha in 'n':
        break
print('-' * 40)
 # Formatting the table
print('cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
# Formatting the table data
for k, v in enumerate(time): 
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
 # Player Search // Number of goals
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para finalizar) -> '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Digite uma opção válida!')
    else:
        print(f'-> DADOS DO JOGADOR {time[busca]["Nome"]}:')
        for v, k in enumerate(time[busca]['Gols']):
            print(f'    No jogo {v + 1} fez {k} gols.')
    print('-' * 40)
print(f'{" PROGRAMA FINALIZADO ":=^40}')