lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #Tupla -> Variável composta
print(sorted(lanche)) # -> sorted significa: Em ordem!
print(lanche)

print('-' * 12)

a = (2, 5, 4 , 6, 7)
b = (3, 8, 1, 2, 5)
c = b + a
print(a)
print(b)
print(sorted(b + a)) #Cuidado com a ordem na hora de juntar as tuplas
print(c.count(5)) #Quantas vezes o número 5 aparece no C
print(c.index(4)) #Serve para ver em qual posição está o número que eu colocar em C
print(c.index(5, 2)) #O ", 2" seria o deslocamento