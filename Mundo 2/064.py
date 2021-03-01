# Treating Multiple Values v1.0
n = 0 #Números
c = 0 #Contador dos números
s = 0 #Soma dos números
print('{:=^54}'.format(' Calculadora! '))
n = int(input('Digite um número para somar [999 para parar]: '))
while n != 999:
    if n != 999:
        c += 1 #Contador
        s += n #Soma
        n = int(input('Digite um número para somar [999 para parar]: ')) #Input
print('Foram contados {0}\nSua soma é: {1}'.format(c, s))
print('=' * 54)