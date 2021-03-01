# Prime numbers
n = int(input('Digite um número: '))
true = ('O número {0} é primo.'.format(n))
false = ('O número {0} não é primo.'.format(n))
if n < 2:
    print(false)
elif n == 2:
    print(true)
elif n % 2 == 0:
    print(false)
else:
    for p in range(3, n // 2, 2):
        if n % p == 0:
            print(false)
            break
    else:
        print(true)