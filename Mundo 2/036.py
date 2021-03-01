# Approving a Loan
casa = float(input('\nQual o valor da casa? R$'))
salário = float(input('Qual o valor do salário? R$'))
ano = int(input('Em quantos anos será pago? '))
parcela = casa / (ano * 12)
minimo = salário * 30 / 100
print('\nPara pagar uma casa em R${0:.2f} em {1:.0f} anos.'.format(casa, ano))
if parcela <= minimo:
    print('O seu crédito foi \033[1;31mReprovado!\033[m')
else:
    print('O seu crédito foi \033[1;32mAprovado!\033[m')