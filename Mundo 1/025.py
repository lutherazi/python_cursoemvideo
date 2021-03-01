# Searching for a string inside another string
nome = input('Digite o seu nome completo: ').strip()
print('O seu nome é: {0}'.format(nome))
print('Seu nome tem Silva? {0}'.format('silva' in nome.lower()))