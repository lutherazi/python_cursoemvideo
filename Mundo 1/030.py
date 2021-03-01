# Odd or Even?
num = int(input('Digite um número: '))
if num % 2 == 0: #Se você dividir um número por 2 e ele não sobrar resto, significa que ele é par, caso contrário seria impar.
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))