# Validating mathematical expressions
# --> A lógica por trás do programa é entender se um parentese que foi aberto, também foi fechado.
# --> Para isso é necessário ter uma lista, nela deverá conter os parenteses que abrem "("
# --> Sempre que um paretentese fechar um aberto, será deletado um elemento já adicionado, no caso o "("
# --> A condição final é se não houver nenhum elemento na lista, dessa forma dando a entender que todos os parenteses foram fechados corretamente.
exp = input('Digite uma expressão matemática: ')
lista = []                      # --> Guarda informações dos paranteses
for c in exp:
    if c == '(':
        lista.append('(')       # --> Adiciona um elemento na lista, no caso o ""
    elif c == ')':              # --> Se o programa reconhecer um ")", ele vai perguntar se há algum elemento na lista
        if len(lista) > 0:     
            lista.pop()         # --> Se houver um elemento na lista, ele vai deleta-lo
        else:
            lista.append(')')   # --> Caso não tenha um valor na lista e mesmo assim encontrar ")", o programa vai adicionar um valor ")" e encerrará o for
            break
if len(lista) == 0:
    print('Sua expressão está correta!')    # --> Caso não tenha nenhum elemento na lista
else:
    print('Sua expressão está incorreta!')  # --> Caso tenha algum elemento na lista