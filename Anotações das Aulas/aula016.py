lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #Tupla -> Variável composta
#Tuplas são imutáveis
#lanche[1] = 'Hamburguer' --> Não funciona
print(len(lanche)) #Quantos tem
print(lanche[0:4]) #Consigo definir o que eu quero ver

for cont in range(0, len(lanche)): #Posso usar a Tupla no for com range também
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('-' * 12)

for comida in lanche: #Posso usar o For dentro da Tupla
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-' * 12)

for pos, comida in enumerate(lanche): #Caso eu queria a posição sem usar o range, usando o enumerate e colocando duas variáveis no for
    print(f'Eu vou comer {comida} na posição {pos}')