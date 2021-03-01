# Analyzing and Generating Dictionaries
def notas(*nt, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param nt: uma ou mais notas dos alunos
    :param sit: valor opcional, indiciando se deve ou não adicionar a situação
    :return: retorna dicionário com várias informações sobre a situação da turma
    '''
    n = dict()
    n['notas'] = len(nt)
    n['maior'] = max(nt)
    n['menor'] = min(nt)
    n['media'] = sum(nt) / len(nt)
    if sit:
        if n['media'] >= 7:
            n['situação'] = 'BOA!'
        elif n['media'] >= 5:
            n['situação'] = 'RAZOÁVEL!'
        else:
            n['situação'] = 'RUIM!'
    return n

# Main Program
resp = notas(5.5, 9.5, 2, 2, sit=True)
resp1 = notas(6, 9, 2, 1, 4)
print(resp)
print(resp1)
help(notas)