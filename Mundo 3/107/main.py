import moeda

print(f'{" Crédito Fácil Azi ":-^40}')
taxa = int(input('Digite o valor da taxa: '))
desc = int(input('Digite o valor do desconto: '))
v = float(input('Valor do emprestimo R$'))
print(f'O valor {v} com taxa de {taxa} fica em {moeda.aumentar(v, taxa):.2f}')
print(f'O valor {v} com desconto de {desc} fica em {moeda.diminuir(v, desc):.2f}')
print(f'O valor {v} tem como dobro {moeda.dobro(v):.2f}')
print(f'O valor {v} tem como metade {moeda.metade(v):.2f}')
print(f'{" PROGRAMA ENCERRADO ":-^40}')