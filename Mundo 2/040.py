# Average calculation
n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
# An average grade above 7 is approved
# An average grade below 5 is a fail
# Average between 5 and 6.9 is recovery
print('Você tirou {0:.1f} e {1:.1f}, a média entre as duas notas é: {2:.1f}.'.format(n1, n2, media))
print('É necessário ter uma média de 7 ou maior para ser aprovado.')
if media < 5:
    print('Você foi \033[;31mreprovado\033[m!\n')
elif media >= 5 and media < 7:
    print('Você está de \033[;33mrecuperação\033[m!\n')
elif media >= 7:
    print('Parabéns, você foi \033[;32maprovado\033[m!\n')