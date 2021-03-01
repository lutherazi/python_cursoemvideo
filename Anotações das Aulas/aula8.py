#AULA DE MÓDULOS IMPORTANDO TODA A BIBLIOTECA
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {0} é: {1}'.format(num, raiz))
print('A raiz de {0} arredondada para cima é: {1}'.format(num, math.ceil(raiz))) #Ou mudo na máscara com :.2f
print('A raiz de {0} arredondada para baixo é: {1}'.format(num, math.floor(raiz)))
print('A raiz de {0} truncada é: {1}'.format(num, math.trunc(raiz)))