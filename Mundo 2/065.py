# Highest and lowest values
resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    print(num)
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Você deseja continuar? [S/N] ').strip()[0]
    if resp not in 'SsNn':
        resp = input('Valor inválido!\nVocê deseja continuar? [S/N] ').strip()[0]
media = soma / quant
print('Com um total de {0} números, a média dos números é: {1:.2f}\nMaior número: {2}\nMenor número: {3}'.format(quant, media, maior, menor))