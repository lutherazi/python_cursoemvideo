# Worker Registration in Python
from datetime import datetime
ficha = dict()
print(f'{" APOSENTADORIA ":=^40}')
ficha['nome']  = input('Nome: ')
nasc           = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - nasc
ficha['ctps']  = input('Carteira de Trabalho (Digite 0 caso não tenha): ')
# If you have a work permit
if ficha['ctps'] != '0':
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: '))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contratação'] + 35) - datetime.now().year)
    print('-' * 40)
    for k, v in ficha.items():
        print(f'- {k}: {v}')
# If you don't have a work permit
else:
    if ficha['ctps'] == '0':
        del ficha['ctps']
        print('-' * 40)
        for k, v in ficha.items():
            print(f'{k} tem o valor de {v}')