# Cathodes and hypotenuse
from math import hypot

a = float(input('Informe o valor do Cateto Oposto: '))
b = float(input('Informe o valor do Cateto Adjacente: '))
c = hypot(a, b)
print('O valor da hipotenusa é: {0:.2f}'.format(c))