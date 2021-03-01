# Player Profile
def ficha(nome='', gols=0):
    if nome.strip() == '':
        nome = r'"Desconhecido"'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Main Program
print(f'{" Ficha do Jogador ":-^40}')
nome = str(input('Nome do jogador: '))
gol  = str(input('Número de Gols: '))
ficha(nome, gol)
print('-' * 40)