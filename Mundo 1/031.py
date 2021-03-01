# Cost of the trip
dis = int(input('Qual a distância da viagem? '))
viagemcara = dis * 0.45 #201
viagembarata = dis * 0.50 #200
if dis <= 200:
    print('Para viagem de {0}KM, o valor da passagem é: R${1:.2f}'.format(dis, viagembarata))
else:
    print('Para viagem de {0}KM, o valor da passagem é: R${1:.2f}'.format(dis, viagemcara))