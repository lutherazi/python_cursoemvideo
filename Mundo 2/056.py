# Complete Analyzer
soma = 0
idade = 0
mulheres = 0
maior = 0
for c in range(1, 5):
    print('---- {0}ª PESSOA ----'.format(c))
    nome = input('Digite o nome das pessoas:\n>>> ')
    idade = int(input('Digite a idade:\n>>> '))
    sexo = int(input('[1] - Masculino / [2] - Feminino\n>>> '))
    soma = soma + idade
    print('--=' * 7)
    if sexo == 2 and idade < 20:
        mulheres = mulheres + 1
    if sexo == 1:
        if idade > 0:
            maior = idade
            nom = nome
        else:
            nome = print('Não tem homem na lista')
#Resolução
media = soma / 4
print('A média da idade do grupo é {0}'.format(media))
print('O nome do homem mais velho é o {0}, sendo a sua idade {1}.'.format(nom, maior))
print('{0} mulheres são menores de idade.'.format(mulheres))