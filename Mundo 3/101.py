# Voting Functions
from datetime import datetime

def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        situação = 'NÃO VOTA'
    elif idade >= 16 and idade < 18 or idade > 65:
        situação = 'VOTO OPCIONAL'
    else:
        situação = 'VOTO OBRIGATÓRIO'
    return print(f'   Com {idade} anos: {situação}')


# Main Program
print('-' * 40)
ano = int(input('   Digite o ano que você nasceu: '))
voto(ano)
print('-' * 40)
