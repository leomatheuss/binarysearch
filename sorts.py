import random

'''
def bubble_sort(array):
    comparacao = 0
    swap = 0
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
               swap += 1
            comparacao += 1

    return print('foram feitas {} comparações e {} swaps'.format(comparacao, swap))
'''
def bubble_sort(array):
    comparacao = 0
    swap = 0
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
               swap += 1
            comparacao += 1

    return array