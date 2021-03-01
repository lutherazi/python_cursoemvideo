# Electronic Radar
vel = float(input('Velocidade: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em: R${0:.2f}, por andar com a velocidade de: {1}KM/H'.format(multa, vel))
else:
    print('Boa viagem! Sua velocidade é de: {0}KM/H'.format(vel))