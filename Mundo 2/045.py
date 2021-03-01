# JO - KEN - PO
import random
from time import sleep
pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
print('''////////////////////////////////
         JO - KEN - PÔ
////////////////////////////////''')
print('''Escolha entre Pedra, Papel e Tesoura:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura''')
# Choices
player_str = int(input('----> '))
if player_str == 1:
    player_choice = pedra
elif player_str == 2:
    player_choice = papel
elif player_str == 3:
    player_choice = tesoura
pc_choice = random.choice([pedra, papel, tesoura]) # Computer Choice

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)

# Player Victory
if player_choice == pedra and pc_choice == tesoura:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nParabéns, você ganhou!'.format(player_choice, pc_choice))
elif player_choice == papel and pc_choice == pedra:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nParabéns, você ganhou!'.format(player_choice, pc_choice))
elif player_choice == tesoura and pc_choice == papel:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nParabéns, você ganhou!'.format(player_choice, pc_choice))

# Computer Victory
if pc_choice == pedra and player_choice == tesoura:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nVocê perdeu!'.format(player_choice, pc_choice))
elif pc_choice == papel and player_choice == pedra:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nVocê perdeu!'.format(player_choice, pc_choice))
elif pc_choice == tesoura and player_choice == papel:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nVocê perdeu!'.format(player_choice, pc_choice))
# Draw
if player_choice == pedra and pc_choice == pedra:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nEmpate!'.format(player_choice, pc_choice))
elif player_choice == papel and pc_choice == papel:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nEmpate!'.format(player_choice, pc_choice))
elif player_choice == tesoura and pc_choice == tesoura:
    print('Você escolheu: {0}\nO computador escolheu: {1}\nEmpate!'.format(player_choice, pc_choice))