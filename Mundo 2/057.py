# Data Validation
sexo = input('''Qual o seu sexo?
[M] -> Masculino
[F] -> Feminino
>>> ''').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados inválidos, tente novamente.\n>>> ')
print('Sexo {0} registrado com sucesso!'.format(sexo))