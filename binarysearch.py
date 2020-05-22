import random
import time

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

def binary_search(vetor, inicio, fim, valor):
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

x = int(input("Valor que deseja encontrar no vetor"))
vetor = random.sample(range(500),500)
vetor_arrumado = bubble_sort(vetor)
binary_search(vetor_arrumado, 0, len(vetor_arrumado)-1, x)
