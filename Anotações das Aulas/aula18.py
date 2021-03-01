teste = list()
teste.append('Luther')
teste.append(22)

galera = list()
galera.append(teste[:])
teste[0] = 'Nilza'
teste[1] = 49
galera.append(teste[:])
print(galera)