# Ranking athletes
from datetime import date

ano_nasc = int(input('\nAno de nascimento: '))
data_atual = date.today().year
idade = data_atual - ano_nasc
print('Em {0} você completa {1} anos.'.format(data_atual, idade))
if idade <= 9:
    print('A sua categoria é: Mirim')
elif idade > 9 and idade <= 14:
    print('A sua categoria é: Infantil')
elif idade > 14 and idade <= 19:
    print('A sua categoria é: Junior')
elif idade >= 20 and idade <= 25:
    print('A sua categoria é: Sênior')
elif idade > 25:
    print('A sua categoria é: Master')