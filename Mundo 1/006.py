# Double, Triple, Square Root
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
s = pow(n, 1/2) #n ** (1/2)
print('O número digitado foi: {0}\nO dobro é: {1}\nO triplo é: {2}\nA raiz quadrada é {3:.2f}'.format(n, d, t, s))