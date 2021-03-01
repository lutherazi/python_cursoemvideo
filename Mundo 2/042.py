# Analyzing Triangles v2.0
r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
true = (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2)
if true: #Verdadeiro caso seja um triângulo
    print('\nOs segmentos formam um triângulo.')
    if true and r1 == r2 == r3: #Equilátero
        print('Os segmentos formam um triângulo escaleno, com todos os lados iguais.\n')
    elif true and r1 != r2 != r3 != r1: #Escaleno
        print('Os segmentos formam um triângulo escaleno, com todos os lados diferentes.\n')
    else: #Isósceles
        print('Os segmentos formam um triãngulo isósceles, com dois lados iguais.\n')
else: #Falso caso não seja um triângulo
    print('\nOs segmentos não formam um triângulo.')