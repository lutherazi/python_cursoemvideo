# Counter Function
    # -> Counting up
    # -> Counting down
    # -> if the "passo" is 0, consider 1
    # -> Recognize negative number
from time import sleep
def contador(início, fim, passo):
    if passo < 0:  # if "passo" is negative, convert in positive
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}.')
    # Counting up
    if início < fim:
        for c in range(início, fim + 1, passo):
            print(f'{c} / ', end='', flush=True)
            sleep(0.3)
        print('Fim!')
        print('-' * 40)
    # Counting down
    if início > fim:
        for c in range(início, fim - 1, -passo):
            print(f'{c} / ', end='', flush=True)
            sleep(0.3)
        print('Fim!')
        print('-' * 40)


# Main Program
# Set Counts
print(f'{" Função de Contador ":-^40}')
contador(0, 10, 1)
contador(10, 0, 2)
# User Interaction
print('Agora é a sua vez de personalizar a contagem!') 
início = int(input('Início: '))
fim    = int(input('Fim: '))
passo  = int(input('Passo : '))
print('-' * 40)
contador(início, fim, passo)