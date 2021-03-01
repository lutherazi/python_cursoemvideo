# Measurement converter
#KM (X / 1000) - HM (X / 100) - DAM (X / 10) - M - DM (X * 10) - CM (X * 100) - MM (X * 1000)
med = float(input('Digite a medida em metro a ser convertido: '))
km  = med / 1000
hm  = med / 100
dam = med / 10
dm  = med * 10
cm  = med * 100
mm  = med * 1000
print('Quilômetro: {0}km\nHectômetro: {1}hm\nDecâmetro: {2}dam'.format(km, hm, dam))
print('Metro: {0}m'.format(med))
print('Decímetro: {0}dm\nCentímetro: {1}cm\nMilímetro: {2}mm'.format(dm, cm, mm))