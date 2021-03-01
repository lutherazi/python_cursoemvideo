# Countdown
from time import sleep

print('<<< FIREWORKS >>>')
soltar = input('''ARE YOU READY?
[Y] - Lauch fireworks!
[N] - I don't know yet!
>>> ''')

if soltar == 'y':
    print("Let's do it, bro!")
elif soltar == 'n':    
    print('Are you sure?')
    sleep(0.5)
    print("I don't care!")
    sleep(0.5)
for c in range(11, 1, -1):
    print(c - 1)
    sleep(0.5)
print('BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!')