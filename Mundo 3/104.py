# Validating data input in Python
def leiaInt(msg):
    ok = False # Condição para parar o While
    valor = 0  # Valor que será convertido
    while True:
        n = str(input(msg)) # Aqui estou dizendo que "n" recebe um input com a mensagem que vai ser dita fora da função
        if n.isnumeric():
            valor = int(n)  # Conversão do valor para o número inteiro que foi digitado na string
            ok = True       # Converte o "ok" para True, sendo a condição de parada do laço
        else:
            print('ERRO! Digite um valor válido!')
        if ok:  # ok = True
            break
    return valor


# Main Program
n = leiaInt('Digite um número: ')
print(f'O número que você digitou é {n}')