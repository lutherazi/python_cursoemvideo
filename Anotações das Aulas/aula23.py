# Tratamento de Erros e Exceções
while True:
    try:
        a = int(input('N1 -> '))
        b = int(input('N2 -> '))
        r = a / b
    except (ValueError, TypeError):
        print(f'Tivemos um problema com os tipos de dados que você digitou.')
    except ZeroDivisionError:
        print(f'Não é possível dividir um número por zero!')
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados!')
    # except Exception as erro: # -> Cria uma variável
    #    print(f'Problema encontrado foi {erro.__class__}')
    else:
        print(f'O resultado é {r}')
        break