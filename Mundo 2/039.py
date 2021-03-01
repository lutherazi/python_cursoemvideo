# Military Enlistment
import datetime

print('--=--' * 10)
print(' ' * 13, 'Alistamento Militar')
print('--=--' * 10)

nasc = int(input('Digite o seu ano de nascimento: '))
data = datetime.datetime.now() #Variável para puxar data atual do computador
ano_atual = int(data.year) #Conversão de str para int
idade = ano_atual - nasc #Calculo da Idade

if idade < 18:
    print('Você está com {0} anos.\nAinda não está na hora de se alistar, volte quando tiver 18 anos.'.format(idade))
    print('--=--' * 10)
elif idade == 18:
    print('Voc~e está com {0} anos.\nChegou a hora de se alistar! Encontre a Junta Militar mais próxima e realize o seu alistamento.'.format(idade))
    print('--=--' * 10)
else:
    print('Você está com {0} anos.\nVocê está atrasado com a sua obrigação militar, vá na Junta Militar e faça o seu alistamento.'.format(idade))
    print('--=--' * 10)