# Menu with tuple 
print('{:=^39}'.format(' Listagem de Preços '))
products = ('Pizza Calabresa', 29.90,
            'Pizza À Moda', 32.90,
            'Pizza 4 Queijos', 29.90,
            'Pizza Frango c/ Catupiry', 32.90,
            'Pizza de Presunto', 26.90,
            'Pizza Marguerita', 24.90,
            'Pizza Italiana', 28.90,
            'Pizza Americana', 28.90,
            'Pizza Lombinho Canadense', 28.90)
for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<31}', end=' ')
    else:
        print(f'R${products[pos]:>5.2f}')
print('=' * 39)