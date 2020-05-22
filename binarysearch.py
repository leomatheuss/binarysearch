import random
import time

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

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
        midrange = inicio + fim // 2
        if x == vetor[midrange]:
            return print(midrange)
        if x < vetor[midrange]:
            fim = midrange - 1
        else:
            inicio = midrange + 1
    
    return -1 #não enncontrado


x = int(input("Valor que deseja encontrar no vetor"))
vetor = random.sample(range(3000),3000)
vetor_arrumado = bubble_sort(vetor)
tam = len(vetor_arrumado)
binary_search2(vetor_arrumado, x, tam)
#binary_search(vetor_arrumado, 0, len(vetor_arrumado)-1, x)
