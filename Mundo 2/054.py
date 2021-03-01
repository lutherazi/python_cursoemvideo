# Majority Group
from datetime import date

year = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {0}ª pessoa nasceu?: '.format(pessoa)))
    idade = year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{0} são maiores de idade e {1} são menores de idade.'.format(maior, menor))