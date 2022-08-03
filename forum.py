#b) Construa uma função que receba uma string como parâmetro e
#devolva outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra python,
#pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
#de forma aleatória.
#Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
#independentemente de como foram digitados.

from random import shuffle #importou biblioteca shuffle

def embaralha(nome): #definiu função
    a = list(nome) #vetor
    shuffle(a) #chamei shuffle
    a = ''.join(a) # Esta junta os caracteres da tupla
    print(a.lower()) #converte letras em caixa alta para minusculas


nome = input('Digite algo: ') 
embaralha(nome)

    
