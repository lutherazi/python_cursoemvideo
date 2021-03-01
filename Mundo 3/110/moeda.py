def aumentar(v=0, taxa=0, formato=False):
    res = v + (v * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(v=0, taxa=0, formato=False):
    res = v - (v * taxa / 100)
    return res if format is False else moeda(res)


def dobro(v=0, formato=False):
    res = v * 2
    return res if format is False else moeda(res)


def metade(v=0, format=False):
    res = v / 2
    return res if format is False else moeda(res)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v=0, aum=0, desc=0):
    print('-' * 40)
    print(f'  - Preço analisado -> \t{moeda(v)}')
    print(f'  - Dobro do preço  -> \t{dobro(v, True)}')
    print(f'  - Metade do preço -> \t{metade(v, True)}')
    print(f'  - Aumento de 10%  -> \t{aumentar(v, aum, True)}')
    print(f'  - Desconto de 5%  -> \t{diminuir(v, desc, True)}')
    return resumo