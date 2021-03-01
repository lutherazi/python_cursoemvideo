f1 = ('Curso em Vídeo Python')
#Análise
print(len(f1))
print(f1.count('o', 0, 14))
print(f1.upper().count('C'))
print(f1.find('deo'))
print(f1.find('Androind'))
print('Curso' in f1)
#Transformação
print(f1.replace('Python', 'Android'))
print(f1.upper())
print(f1.lower())
print(f1.capitalize()) #Só o primeiro caractere fica em maiusculo
print(f1.title()) #Todos os primeiros caracteres ficam em maiusculo
###
print('-' * 12)
###
#Apagando Espaços
f2 = ('   Aprendendo Python  ')
print(f2.strip())
print(f2.rstrip())
print(f2.lstrip())
###
print('-' * 12)
###
#Divisão
print(f1.split())
#Junção
print('-'.join(f1))