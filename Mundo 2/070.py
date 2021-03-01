# Statistic on Products
cheap = 0
total = 0
tooprice = 0 
amount = 0
product = ''
print('{:=^40}'.format(' LOBO STORE! '))
while True:
    name = input('Digite o nome do produto: ').upper().strip()
    price = float(input('Digite o valor do produto: R$'))
    total += price
    amount += 1
    if amount == 1 or price < cheap: # Cheapest Product
        cheap = price
        product = name
    if price > 1000: # Expensive Products
        tooprice += 1
    keep = ' '
    while keep not in 'SN':
        keep = input('Você deseja continuar? [S/N] ').upper().strip()[0]
    if keep == 'N':
        break
    print('=' * 40)
print('''A) Gasto total de: R${0:.2f}
B) {1} produtos custam mais que R$1000.00
C) O produto mais barato é: {2}, custando: R${3:.2f}'''.format(total, tooprice, product, cheap))
print('{:=^40}'.format(' COMPRA FINALIZADA '))