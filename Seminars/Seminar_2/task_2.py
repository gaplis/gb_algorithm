# Сортировка подсчетами (Counting Sort) - это алгоритм сортировки, 
# который использует подсчет количества каждого элемента в массиве и сортировку по вспомогательному массиву.

# Отсортируйте массив целых не отрицательных чисел.
# Гарантируется, что минимальный элемент равен 0. Максимальный элемент может меняться.

import time
import random
from task_1 import quick_sort

m = 100000
n = 1000000

nums = [random.randint(1, m) for _ in range(n)]

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1
    result = []
    for i, c in enumerate(count):
        result += [i] * c
    return result

start_time = time.time()
counting_sort(nums)
end_time = time.time()
print('counting_sort', end_time - start_time)

start_time2 = time.time()
quick_sort(nums)
end_time2 = time.time()
print('quick_sort', end_time2 - start_time2)
