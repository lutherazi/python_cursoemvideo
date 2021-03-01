# Large Number
print('{:=^40}'.format(' NÚMERO POR EXTENSO! '))
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quartoze',
            'quinze' 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente: '))
    break
print('O número que você digitou foi: {0}\nPor extenso é: {1}'.format(num, contagem[num].upper()))