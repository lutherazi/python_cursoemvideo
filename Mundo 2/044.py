# Payment Management
print('{:=^40}'.format(' LOJAS AZI '))
valor = float(input('Digite o valor do produto: R$'))
forma = int(input('''FORMAS DE PAGAMENTO:
[1] - À Vista no Dinheiro/Cheque
[2] - À Vista no Cartão de débito
[3] - 2x no Cartão de Crédito
[4] - 3x ou mais no Cartão de Crédito
>>> '''))
while True:
    if forma == 1:
        total = valor - (valor * 10 / 100)
        print('O produto de R${0:.2f}, com 10% de desconto vai sair em: R${1:.2f}'.format(valor, total))
        break
    elif forma == 2:
        total = valor - (valor * 5 / 100)
        print('O produto de R${0:.2f}, com 5% de desconto vai sair em:R${1:.2f}'.format(valor, total))
        break
    elif forma == 3:
        total = valor / 2
        print('O produto de R${0:.2f}, sairá em 2x de R${1:.2f}'.format(valor, total))
        break
    elif forma == 4:
        parcela = float(input('Digite o número de parcelas: '))
        total = valor / parcela
        print('O produto de R${0:.2f}, sairá em {1}x de R${2:.2f}'.format(valor, parcela, total))
        break
    else:
        del(forma)
        forma = int(input(('Opção inválida!\nDigite uma opção válida.\n>>> ')))