import moeda

print(f'{" Crédito Fácil Azi ":-^40}')
taxa = int(input('Digite o valor da taxa: '))
desc = int(input('Digite o valor do desconto: '))
v = float(input('Valor do emprestimo R$'))
print('-' * 40)
print(f'Aumentando {taxa}% temos {moeda.aumentar(v, taxa, True)}')
print(f'Descontando {taxa}% temos {moeda.diminuir(v, taxa, True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}')
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}')
print(f'{" PROGRAMA ENCERRADO ":-^40}')