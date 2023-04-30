# 1.Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и указать признаки квадратичной сложности для каждого из них.
# 4.Написать алгоритм быстрого поиска (quicksort).

import time
import random

nums = [random.randint(1, 10000) for _ in range(1, 1000)]

print(nums)

def bubble_sort(nums):
    for j in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

start_time = time.time()
print(bubble_sort(nums))
end_time = time.time()
print(end_time - start_time)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)

    less_arr = [n for n in arr if n < pivot]
    e_arr = [pivot] * arr.count(pivot)
    b_arr = [n for n in arr if n > pivot]
    return quick_sort(less_arr) + e_arr + quick_sort(b_arr)

start_time = time.time()
print(quick_sort(nums))
end_time = time.time()
print(end_time - start_time)

