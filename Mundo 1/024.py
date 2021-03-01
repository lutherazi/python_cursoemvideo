# Checking the first letters of a text
cid = input('Digite sua cidade: ').strip().lower()
print('Sua cidade é: {0}'.format(cid))
print('Sua cidade começa com o nome Santo? {0}'.format('santo' in cid))