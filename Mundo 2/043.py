# Body Mass Index (BMI)
print('---' * 19)
print('De acordo com a tabela abaixo, vamos descobrir o seu IMC:')
print('''Abaixo do peso    | IMC abaixo de 18.5
Peso Ideal        | IMC entre 18.5 e 25
Sobrepeso         | IMC de 25 até 30
Obesidade         | IMC de 30 até 40
Obesidade Mórbida | IMC acima de 40''')
print('---' * 19)
peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / altura ** 2
print('Seu peso é: {0}Kg'.format(peso))
print('Sua altura é: {0}m'.format(altura))
print('---' * 19)
if imc < 18.5: # Underweight
    print('IMC: {0:.1f}\nVocê está abaixo do peso.\n'.format(imc))
elif imc >= 18.5 and imc < 25: # Ideal weight
    print('IMC: {0:.1f}\nVocê está no peso ideal.\n'.format(imc))
elif imc >= 25 and imc < 30: # Overweight
    print('IMC: {0:.1f}\nVocê está com sobrepeso.\n'.format(imc))
elif imc >= 30 and imc < 40: #Obesity
    print('IMC: {0:.1f}\nVocê está na condição de Obesidade.\n'.format(imc))
elif imc >= 40: # Morbid obesity
    print('IMC: {0:.1f}\nVocê está na condição de Obesidade Mórbida.\n'.format(imc))