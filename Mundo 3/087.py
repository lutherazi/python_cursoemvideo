# More about Matrix in Python
print(f'{"Matriz 3x3!":-^40}')
matriz     = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_y = 0
# User interaction with the matrix
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_y += matriz[l][c]
# Formatting the Matrix
print(f'{"MATRIZ":-^40}')
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end='')
    print()
print(f'{"Resultado:":-^40}')
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_y}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')