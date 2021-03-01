# Cost of the trip
dist = float(input('\nQual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {0}Km.'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço da sua passagem será de R${:.2f}\n'.format(preco))