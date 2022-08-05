#quick sort
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <=pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

    #inserction sort
    	
        def insertionsort(lista, inicio=0, fim=None):
2	    n = len(lista)
3	    for i in range(1, n):
4	        valor_inserir = lista[i] 
5	        j = i - 1
6	        
7	        while j >= 0 and lista[j] > valor_inserir:
8	            lista[j + 1] = lista[j]
9	            j -= 1
10	        lista[j + 1] = valor_inserir
11	    
12	    return lista
13	