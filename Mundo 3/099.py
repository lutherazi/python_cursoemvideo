# Function that finds the bigger
from time import sleep
def maior(* núm):
    cont = maior = 0
    print(f'{" Analisando ":-^40}')
    sleep(0.5)
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'- Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Main Program
print(f'{" Função com Maior número ":-^40}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print(f'{" Volte Sempre! ":-^40}')