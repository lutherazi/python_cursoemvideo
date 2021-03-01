# Prime numbers
primeiro = int(input('Digite o primeiro número da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = primeiro + (10 - 1) * razao
ultimo = ultimo + 1
for c in range(primeiro, ultimo, razao):
    print(c, end=' > ')
print('Acabou!')