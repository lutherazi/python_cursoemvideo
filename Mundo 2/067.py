# Multiplication Table v3.0
print('{:=^40}'.format(' TABUADA v3.0 '))
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for c in range(1, 11): #Tabuada
        print('{0} x {1:2} = {2}'.format(num, c, num * c))
    print('=' * 40)
print('{:=^40}'.format(' PROGRAMA FINALIZADO'))