# Painting wall
# BASE X ALTURA, ÁREA / 2
tinta = float(input('Quantos litros por m², sua lata de tinta gasta? '))
b = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = b * h
tinta_gasta = a / tinta
print('-' * 12)
print('A dimensão da sua parede é de {0}x{1}, sendo a área {2}m².'.format(b, h, a))
print('A quantidade de tinta necessária para pintar tal parede é de: {0}L por m²'.format(tinta_gasta))
print('-' * 12)