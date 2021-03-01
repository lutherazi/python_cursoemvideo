# Odd sum multiples of three
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c #ou soma += c
        cont = cont + 1
print('A soma de {0} valores que são múltiplos de três entre 1 e 500 é: {1}.'.format(cont, s))