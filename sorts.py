import random
import time
import sys

sys.setrecursionlimit(300000)

def bubble_sort(array):
    comeco = time.time()
    comparacao = 0
    swap = 0
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
               swap += 1
            comparacao += 1
    fim = time.time()
    print('tempo de execucao {} '.format(fim-comeco))
    return print("O algoritmo fez {} comparacoes e realizou {} swaps".format(comparacao,swap))

def particao(array, start, stop):
    
    i = (start -1)
    pivot = array[stop]
    for j in range(start, stop):
        if array[j] <= pivot:
            i += 1
            array[j],array[j] = array[j],array[i]
    array[i+1], array[stop] = array[stop], array[i+1]
    
    return(i+1)

def quicksort(array, start, stop):
    
    if start < stop:
        part_index = particao(array, start, stop)

        quicksort(array, start, part_index-1)
        quicksort(array, part_index+1, stop)

