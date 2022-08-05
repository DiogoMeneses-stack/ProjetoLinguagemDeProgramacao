
#usando funcao len() e in para saber se esse código está no sequencia ou não;
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

print("=====================================================\n")

#usando Funcao split() ela corta o texto
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")
palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

print("=====================================================")

#Lista
vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas
for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

print("=====================================================")

#List comprehension (Compreensões de lista)

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo
#resultado que a linha 1
#Esse tipo de técnica é utilizada quando, dada uma sequência,
#deseja-se criar uma nova sequência, porém com as informações originais
#transformadas ou filtradas por um critério.

print("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp = ", linguagens)

print("=====================================================")

#A funcao map() é utilizada para aplicar uma
#determinada função em cada item de um objeto iterável.

print("Exemplo")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

print("=====================================================")

#funcao range()

numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

print("====================================================")

# Usando Tuplas
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

print("====================================================")

#Set()
vogais_1 = {'aeiou'} # sem uso do construtor
print(type(vogais_1), vogais_1)
vogais_2 = set('aeiouaaaaaa') # construtor com string
print(type(vogais_2), vogais_2)
vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print(type(vogais_3), vogais_3)
vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print(type(vogais_4), vogais_4)
print(set('banana'))

print("====================================================")

#mapping()
# Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor
dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30
# Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
dici_2 = {'nome': 'João', 'idade': 30}
# Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
dici_3 = dict([('nome', "João"), ('idade', 30)])

print("====================================================")
#Objetos do tipo array NumPy
from concurrent.futures import Executor
from sys import executable
import numpy

matriz_1_1 = numpy.array([1, 2, 3]) # Cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # Cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Cria matriz 2 linhas e 3 colunas
print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)

print("===========================================================")

#Algoritmo de busca
def executar_busca_linear(lista, valor):
  for elemento in lista:
    if valor == elemento:
        return True
  return False

import random

lista = random.sample(range(100), 20)
print(sorted(lista))
executar_busca_linear(lista, 10)

print("======================================================")

vogais = 'aeiou'

resultado = vogais.index('e')
print(resultado)

print("======================================================")

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor centra
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
     return False # Se chegar até aqui, significa que o valor não foi encontrado

lista = list(range(1, 50))

print(lista)

print('\n', executable _busca_binaria(lista=lista, valor=60))
print('\n', Executor _busca_binaria(lista=lista, valor=70))

