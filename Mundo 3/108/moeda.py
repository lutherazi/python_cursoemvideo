def aumentar(v=0, taxa=0):
    res = v + (v * taxa / 100)
    return res


def diminuir(v=0, taxa=0):
    res = v - (v * taxa / 100)
    return res


def dobro(v=0):
    res = v * 2
    return res


def metade(v=0):
    res = v / 2
    return res


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')