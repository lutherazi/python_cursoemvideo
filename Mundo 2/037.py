# Numerical bases converter
print('--=--' * 10)
num = int(input('Digite um número qualquer: '))
digito = int(input('Escolha uma dessas opções: \n[1] - Binário \n[2] - Octal \n[3] - Hexadecimal\n--> '))
if digito == 1:
    print('O número {0} convertido para binário é: {1:08b}'.format(num, num)) #Conversão Binária
elif digito == 2:
    print('O número {0} convertido para Octal é: {1:08o}'.format(num, num)) #Conversão Octal
elif digito == 3:
    print('O número {0} convertido para Hexadecimal é: {1:08x}'.format(num, num)) #Conversão Hexadecimal
else:
    print('Opção inválida! Tente novamente.')
print('--=--' * 10)