# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:21:11 2024

@author: HomePC
"""
# we use numPY to generate random arrays.
# matplotlib to plot the result
import numpy as np
import time
import copy
import matplotlib.pyplot as plt

# Generate random arrays of sizes 100, 1000, and 10000
array_sizes = [100, 1000, 10000]
arrays = {size: np.random.randint(0, 10000, size) for size in array_sizes}

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Measure execution time for each sorting algorithm on each array size.
execution_times = {
    'Selection Sort': [],
    'Merge Sort': [],
    'QuickSort': []
}

for size in array_sizes:
    for sort_name, sort_func in zip(['Selection Sort', 'Merge Sort', 'QuickSort'], [selection_sort, merge_sort, quick_sort]):
        arr = copy.deepcopy(arrays[size])
        start_time = time.time()
        if sort_name == 'QuickSort':
            sort_func(arr)
        else:
            sort_func(arr)
        end_time = time.time()
        execution_times[sort_name].append(end_time - start_time)

# Plot the results
for sort_name in execution_times:
    plt.plot(array_sizes, execution_times[sort_name], label=sort_name)

plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()
