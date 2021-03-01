# Bulletin with composite lists
boletim = list()
while True:
    nome  = input('Digite o nome do aluno: ')     # Nome
    nota1 = float(input('Primeira nota: '))       # Nota 1
    nota2 = float(input('Segunda nota: '))        # Nota 2
    média = (nota1 + nota2) / 2                   # Média das notas
    boletim.append([nome, [nota1, nota2], média])
    escolha = input('Você deseja continuar? [S/N] >> ')
    if escolha in 'Nn':
        break
# Formatting
print('-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for key, value in enumerate(boletim):
    print(f'{key:<4}{value[0]:<10}{value[2]:>8.1f}')
print('-' * 30)
# Result
while True:
    opção = int(input('Deseja ver as notas de qual aluno? (999 Interrompe): '))
    if opção == 999:
        print('<<< Programa encerrado! >>>')
        break
    if opção <= len(boletim) - 1:
        print(f'Notas de {boletim[opção][0]} são {boletim[opção][1]}')
print('<<< Volte sempre! >>>')