import moeda

print(f'{" Crédito Fácil Azi ":-^40}')
taxa = int(input('Digite o valor da taxa: '))
desc = int(input('Digite o valor do desconto: '))
v = float(input('Valor do emprestimo R$'))
print('-' * 40)
print(f'Aumentando {taxa}% temos {moeda.moeda(moeda.aumentar(v, taxa))}')
print(f'Descontando {taxa}% temos {moeda.moeda(moeda.diminuir(v, desc))}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'{" PROGRAMA ENCERRADO ":-^40}')