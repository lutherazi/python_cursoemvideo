# Group Data Analysis
adult = 0 # People who are over 18 years old
man = 0   # Registered Men
woman = 0 # Registered women under 20 years old
print('{:=^40}'.format(' CADASTRO '))
while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'MF':
        gender = input('Sexo [M/F]: ').strip().upper()[0]
    if age >= 18:
        adult += 1
    if gender == 'M':
        man += 1
    if gender == 'F' and age < 20:
        woman += 1
    keep = ' '
    while keep not in 'SN':
        keep = input('Você deseja continuar? [S/N] ').strip().upper()[0]
    if keep == 'N':
        break
    print('=' * 40)
print('Há {0} adultos cadastrados\nHá {1} homem(s) cadastrados\nHá {2} mulheres cadastradas com menos de 20 anos.'.format(adult, man, woman))
print('=' * 40)