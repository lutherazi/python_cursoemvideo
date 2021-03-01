# First and last occurrence of a string
frase = input('Digite a sua frase: ').strip()
f_cap = (frase.lower())
print(frase)
print('A letra A aparece um total de: {0}\nAparecendo primeiro na posição: {1}\nAparecendo por último na posição {2}'.format(f_cap.count('a'), f_cap.find('a'), f_cap.rfind('a')))