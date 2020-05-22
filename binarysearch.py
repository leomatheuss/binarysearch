import random
import time
from sorts import bubble_sort, quicksort
import sys

sys.setrecursionlimit(300000)
def binary_search(vetor, inicio, fim, valor):
    '''
    Implementação recursiva
    '''
    i = fim - inicio // 2
    if vetor[i] == valor:
        return print(i)
    elif inicio == fim:
        return print("Valor inexistente no vetor")
    else:
        if vetor[i] < valor:
            binary_search(vetor, i + 1, fim, valor)
        else:
            binary_search(vetor, inicio, i-1, valor)


def binary_search2(vetor, x, tam):
    '''
    Implementação iterativa
    '''
    inicio = 0
    fim = len(vetor) -1
    midrange = 0

    while inicio <= fim:
        midrange = (inicio + fim )// 2
        if x == vetor[midrange]:
            return print(midrange)
        if x < vetor[midrange]:
            fim = midrange - 1
        else:
            inicio = midrange + 1

    return -1 #não enncontrado


#x = int(input("Valor que deseja encontrar no vetor"))
vetor = random.sample(range(20000),20000)   #cria um vetor
vetor2 = vetor.copy()
#vetor_arrumado = bubble_sort(vetor) #chama o bubble sort

#tam = len(vetor_arrumado)
tama = len(vetor)
#print(vetor)
#bubble_sort(vetor2)
#print(vetor)
t1 = time.time()
quicksort(vetor, 0,tama-1)
t2 = time.time()
print('O algoritmo quicksort levou {} para organizar o vetor'.format(t2-t1))
#binary_search2(vetor_arrumado, x, tam) #chama a função de busca binaria iterativa

#binary_search(vetor_arrumado, 0, len(vetor_arrumado)-1, x)
