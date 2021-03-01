# Analyzing Triangles
sal = float(input('Qual é o salário: R$'))
if sal <= 1250:
    new = sal + (sal * 15 / 100)
else:
    new = sal + (sal * 10 / 100)
print('Quem ganhava R${0:.2f}, passa a ganhar R${1:.2f}'.format(sal, new))