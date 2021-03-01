# Multiple numbers with flag
print('{:=^40}'.format(' Para interromper digite: 999 '))
cont = soma = 0
while True:
    num = int(input('Digite o valor: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram contados {cont} números.\nA soma entre eles é: {soma}')