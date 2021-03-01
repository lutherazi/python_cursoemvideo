# Coin Converter
r = float(input('Valor: R$'))
d = r * 5.19
comprar_d = r / 5.19
print('Conversão em dólar: {0:.2f}'.format(d))
print('Com R${0:.2f}, você poderá comprar: ${1:.2f}.'.format(r, comprar_d))