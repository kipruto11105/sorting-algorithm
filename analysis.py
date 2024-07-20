# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:41:16 2024

@author: HomePC
"""

import random
import time

# Function to create a random array
def create_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Selection Sort with comparison count
def selection_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

# Merge Sort with comparison count
def merge_sort(arr):
    comparisons = [0]  # use list to pass by reference

    def merge(left, right):
        merged = []
        while left and right:
            comparisons[0] += 1
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left or right)
        return merged

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    arr[:] = sorted_arr
    return comparisons[0]

# QuickSort with comparison count
def quicksort(arr):
    comparisons = [0]  # use list to pass by reference

    def sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        comparisons[0] += len(arr) - 1  # number of comparisons in partition
        return sort(left) + middle + sort(right)

    sorted_arr = sort(arr)
    arr[:] = sorted_arr
    return comparisons[0]

# Function to measure execution time and comparisons
def measure_sorting_performance(arr, sort_func):
    arr_copy = arr[:]
    start_time = time.time()
    comparisons = sort_func(arr_copy)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # convert to milliseconds
    return execution_time, comparisons

# Main analysis function
def analyze_sorting_algorithms():
    sizes = [100, 1000, 10000]
    results = {size: {} for size in sizes}

    for size in sizes:
        random_array = create_random_array(size)
        print(f"Analyzing array size: {size}")

        for sort_name, sort_func in [("Selection Sort", selection_sort), 
                                     ("Merge Sort", merge_sort), 
                                     ("QuickSort", quicksort)]:
            exec_time, comparisons = measure_sorting_performance(random_array, sort_func)
            results[size][sort_name] = (exec_time, comparisons)
            print(f"{sort_name} - Time: {exec_time:.2f} ms, Comparisons: {comparisons}")

    return results

# Run the analysis
results = analyze_sorting_algorithms()
print("\nFinal Results:")
for size, data in results.items():
    print(f"\nArray Size: {size}")
    for sort_name, metrics in data.items():
        print(f"{sort_name} - Time: {metrics[0]:.2f} ms, Comparisons: {metrics[1]}")
