# First and last name of a person
nome = input('Digite o seu nome completo: ').strip().split()
print('Seu nome completo: {0}'.format(nome))
print('Primeiro nome: {0}'.format(nome[0]))
print('Segundo nome: {0}'.format(nome[-1]))