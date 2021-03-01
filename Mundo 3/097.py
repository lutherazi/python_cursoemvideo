# Especial Print
def write(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


# Main Program
print(f'{" Print Especial ":-^40}')
write('Luther Fiaia Azi')
write('Hello World!')
write('Eu sou um mafioso, como descobriu?')
print(f'{" Volte Sempre! ":-^40}')