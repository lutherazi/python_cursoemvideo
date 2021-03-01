#Primeiro Algorítimo
'''cont = 1
while True: #O true faz o laço rodar infinitamente
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

#Segundo Algorítimo
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma dos valores é {0}'.format(s))
