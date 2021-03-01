# Function that calculates area
def área(a, b):
    resultado = a * b
    print(f'A área de um terreno {a}x{b} é de {resultado}m².')


# Main Program
print(f'{" Área de terreno ":-^40}')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
área(a, b)
print(f'{" Volte Sempre! ":-^40}')