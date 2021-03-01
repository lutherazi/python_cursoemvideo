# Vowel Counter
words = ('a', 'vida', 'nao', 'passa', 'de', 'uma', 'viagem', 'e', 'nela', 'somos', 'passageiros')
for c in words:
    print(f'\nNa palavra {c.upper()} temos as vogais ', end='')
    for letter in c:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')