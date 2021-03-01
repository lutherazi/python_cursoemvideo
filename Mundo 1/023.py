# Number Analyzer
# Only numbers bigger than 999
print('-' * 40)
num = int(input('Digite o número maior que 999: '))
n = str(num) # Int to String
print('-' * 40)
print('O número é: {0}'.format(num))
print('A sua unidade é: {0}'.format(n[3]))
print('A sua dezena é: {0}'.format(n[2]))
print('A sua centena é: {0}'.format(n[1]))
print('O seu mihar é: {0}'.format(n[0]))

# Only numbers smaller than 1000
num = int(input('Digite o número menor que 1000: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
print('O número é: {0}'.format(num))
print('A sua unidade é: {0}'.format(u))
print('A sua dezena é: {0}'.format(d))
print('A sua centena é: {0}'.format(c))