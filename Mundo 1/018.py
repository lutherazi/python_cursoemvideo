# Sine, Cosine and Tangent
from math import sin, cos, tan, radians

a = float(input('Digite o valor do ângulo: '))
print('Seno: {0:.2f}'.format(sin(radians(a))))
print('Cosseno: {0:.2f}'.format(cos(radians(a))))
print('Tangente: {0:2f}'.format(tan(radians(a))))