# Creating an Options Menu
from time import sleep
print('{:=^40}'.format('Faz Tudo'))
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('=' * 40)
    menu = int(input('O que você deseja fazer?\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior número\n[4] - Novos números\n[5] - Sair do programa\n>>> '))
    if menu == 1:   # Sum of the values
        soma = n1 + n2
        print('A soma entre {0} e {1} é igual a: {2}'.format(n1, n2, soma))
    elif menu == 2: # Product of the values
        produto = n1 * n2
        print('Multiplicando o número {0} e {1} resultará em: {2}'.format(n1, n2, produto))
    elif menu == 3: # Major or minor
        if n1 > n2:
            print('O número {0} é maior que {1}'.format(n1, n2))
        elif n2 > n1:
            print('O número {0} é maior que {1}'.format(n2, n1))
        else:
            print('O número {0} é igual a {1}'.format(n1, n2))
    elif menu == 4: # Enter new values
        print('>>>Digite os novos valores:<<<')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu > 5: # Invalid option
        menu = 0
        print('Opção inválida!')
    sleep(1)
print('{:=^40}'.format('Programa encerrado'))