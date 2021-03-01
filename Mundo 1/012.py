# Calculating discounts
preço = float(input('Digite o valor do produto: R$'))
new_preço = preço - (preço * 0.05) #OU -> preço - preço*5/100
print('O antigo preço é de: R${0:.2f}, já o valor do produto com desconto é: R${1:.2f}. O desconto total foi de: R${2:.2f}'.format(preço, new_preço, preço * 0.05))