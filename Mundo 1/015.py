# Car Rental
km_préaluguel = float(input('Quantidade de Km antes do aluguel? '))
km_pósaluguel = float(input('Quantidade de Km pós aluguel? '))
diasdealuguel = int(input('Dias de de aluguel: '))
valorpago = ((km_pósaluguel - km_préaluguel) * 0.15) + diasdealuguel * 60
print('Valor por Km rodado: R${0:.2f}\nValor por dias corridos: R${1:.2f}\nO valor do total do aluguel: R${2:.2f}'.format((km_pósaluguel - km_préaluguel) * 0.15, diasdealuguel * 60, valorpago))