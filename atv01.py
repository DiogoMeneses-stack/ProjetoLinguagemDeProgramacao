#Atv 01

#Vamos criar uma solução que procura pelas vogais “A", “o" em
#um texto. Toda vez que essas letras são encontradas, devemos
#informar que encontramos e qual posição do texto ela está. Nosso
#texto será

texto = """
A inserção de comentários no código do programa é uma prátic
a normal.
Em função disso, toda linguagem de programação tem alguma
maneira de permitir que comentários sejam inseridos nos progr
amas.
O objetivo é adicionar descrições em partes do código, seja par
a documentá-
lo ou para adicionar uma descrição do algoritmo implementado
(BANIN, p. 45, 2018)."
"""

for i, c in enumerate(texto):
    if c == 'A' or c == 'o':
        print(f"Vogal '{c}' encontrada, na posição {i}")
    else:
        continue
