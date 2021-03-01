# Major and minor of the sequence
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {0}ª (kg): '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é: {0}Kg, sendo o menor peso: {1}Kg'.format(maior, menor))