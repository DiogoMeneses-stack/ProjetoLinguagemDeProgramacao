print("Hello World")

print(" ========= ")

#reconhecimento de variáveis type()
x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))


print("=========")

#Entrada de dados input()
nome = input("Digite um nome: ")
print(nome)


print("============")

nome = input("Digite um nome: ")

print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro heeloWorld"%(nome))

#Função format
print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world.")

print("===========")


# Qual o resultado armazenado na variável operacao_1: 25 ou 17?
operacao_1 = 2 + 3 * 5
# Qual o resultado armazenado na variável operacao_2: 25 ou 17?
operacao_2 = (2 + 3) * 5
# Qual o resultado armazenado na variável operacao_3: 4 ou 1?
operacao_3 = 4 / 2 ** 2
# Qual o resultado armazenado na variável operacao_4: 1 ou 5?
operacao_4 = 13 % 3 + 4
print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")

print("============================================")

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")
print(type(a))
print(type(b))
print(type(c))
print(type(x))

print("============================================")

x = float(x) # aqui fazemos a conversão da string para o tipo numérico
y = a * x ** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")
print(type(a))
print(type(b))
print(type(c))
print(type(x))

print("---------------------------------")

#Estrutura condicional simples:
a = 5
b = 10

if a < b:
        print("a é menor do que b")
r = a + b
print(r)

print("=================================")

#Estrutura composta:
a = 10
b = 5

if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
print(r)

print("================================")
#Estrutura encadeada, devemos usar o
#comando "elif", que é uma abreviação de
#else if.
#codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

print("=========================")

#qtde_faltas = int(input("Digite a quantidade de faltas: "))
#media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

print("================")

A = 15
B = 9
C = 9

print(B == C or A < B and A < C)

print((B == C or A < B) and A < C )

print("=============================")


numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Número par!")
else:
    print("Número ímpar!")

print("=============================")

#Com o comando for, podemos usar a função
#enumerate() para retornar à posição de cada
#item, dentro da sequência. Considerando o
#exemplo dado, no qual atribuímos a variável
#"nome" o valor de "Guido", "G" ocupa a
#posição 0 na sequência, "u" ocupa a posição 1,
#"i" a posição 2, e assim por diante. Veja que a
#variável "i" é usada para capturar a posição e a
#variável "c" cada caractere da palavra.

nome = "Guido"

for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")

print("===============================")


