# Highest and lowest values
a = int(input('\nPrimeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Lowest
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Highest
maior = a
if b > a and b > c:
    maior =  b
if c > a and c > b:
    maior = c

# Result
print('\nO menor número é: {0}\nO maior número é: {1}'.format(menor, maior))