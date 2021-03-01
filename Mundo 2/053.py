# Palindrome Detector
frase = input('Digite a frase: ').strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for l in range(len(juntos) -1, -1, -1):
    inverso += juntos[l]
print('O inverso de {0} é {1}.'.format(juntos, inverso))
if inverso == juntos:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')