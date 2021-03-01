# Interactive Python help system
from time import sleep

c = ('\033[m',        # 0 - No color
     '\033[0;30;41m', # 1 - Red
     '\033[0;30;42m', # 2 - Green
     '\033[0;30;43m', # 3 - Yellow
     '\033[0;30;44m', # 4 - Blue
     '\033[0;30;45m', # 5 - Purple
     '\033[7;30m'     # 6 - White 
    );
def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Main Program
comando = ''
while True:
    título('Sistema de Ajuda - Python', 2)
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Programa encerrado!', 1)