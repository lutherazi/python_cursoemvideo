# Text Analyzer
nome = input('Digite o seu nome completo: ').strip()
nome_lista = nome.split()
print('Seu nome em maiusculo é: {0}'.format(nome.upper()))
print('Seu nome em minusculo é: {0}'.format(nome.lower()))
print('Seu nome tem ao todo {0} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {0} e ele tem letras {1}.'.format(nome_lista[0], len(nome_lista[0])))
print('Seu primeiro nome tem {0} letras.'.format(nome.find(' ')))