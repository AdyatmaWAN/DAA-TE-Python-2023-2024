import random
import time
import os
import tracemalloc


def quick_sort(arr, left, right):
    sorted_arr = randomized_quick_sort(arr, left, right)
    return sorted_arr

def randomized_quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        randomized_quick_sort(arr, left, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, right)
    return arr

def partition(arr, left, right):
    random_index = random.randint(left, right)
    arr[right], arr[random_index] = arr[random_index], arr[right]
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def clustered_binary_insertion_sort(arr):
    pop = 0
    for i in range(1, len(arr)):
        cop = i
        key = arr[cop]
        if key >= arr[pop]:
            place = binary_loc_finder(arr, pop+1, cop - 1, key)
        else:
            place = binary_loc_finder(arr, 0, pop - 1, key)
        pop = place
        arr = place_inserter(arr, place, cop)
    return arr

def binary_loc_finder(arr, start, end, key):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start
    else:
        middle = (start + end) // 2
        if arr[middle] < key:
            return binary_loc_finder(arr, middle + 1, end, key)
        elif arr[middle] > key:
            return binary_loc_finder(arr, start, middle - 1, key)
        else:
            return middle

def place_inserter(arr, start, end):
    temp = arr[end]
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]
    arr[start] = temp
    return arr

def generate_random_numbers(n):
    return [random.randint(0, 8191) for _ in range(n)]

def generate_sorted_numbers(n):
    numbers = generate_random_numbers(n)
    numbers.sort()
    return numbers

def generate_reverse_sorted_numbers(n):
    numbers = generate_sorted_numbers(n)
    numbers.reverse()
    return numbers

def save_numbers_to_file(numbers, file_name):
    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def read_numbers_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

def generate():
    m = 20
    for i in range(1, 4):
        n = 10**i
        l = m * n
        for j in range(3):
            random_numbers = generate_random_numbers(l)
            sorted_numbers = generate_sorted_numbers(l)
            reverse_sorted_numbers = generate_reverse_sorted_numbers(l)

            # Save random, sorted, and reverse sorted numbers to text files
            save_numbers_to_file(random_numbers, f'data/random_numbers_{l}_{j}.txt')
            save_numbers_to_file(sorted_numbers, f'data/sorted_numbers_{l}_{j}.txt')
            save_numbers_to_file(reverse_sorted_numbers, f'data/reverse_sorted_numbers_{l}_{j}.txt')

# generate() ## Uncomment this line to generate random, sorted, and reverse sorted numbers

n = [200, 2000, 20000]
m = ["random_numbers", "sorted_numbers", "reverse_sorted_numbers"]

tracemalloc.start()

for i in range(3):
    for j in range(3):
        for k in range(3):
            file_path = f"data/{m[i]}_{n[j]}_{k}.txt"
            arr = read_numbers_from_file(file_path)

            # before_memory_usage = process.memory_info().rss / (1)
            start_time = time.time() * 1000
            tracemalloc.reset_peak()
            sorted_arr = quick_sort(arr, 0, len(arr) - 1)
            current, peak = tracemalloc.get_traced_memory()
            end_time = time.time() * 1000
            tracemalloc.reset_peak()
            # after_memory_usage = process.memory_info().rss / (1)
            execution_time = end_time - start_time

            save_numbers_to_file(sorted_arr, f"result/Randomized_Quick_Sort_{m[i]}_{n[j]}_{k}.txt")

            print("Sorted array using Randomized Quick Sort")
            print("Execution Time: {:.3f} ms".format(execution_time))
            # print("Memory Usage: {:.6f} B".format(after_memory_usage - before_memory_usage))
            print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
            print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))

            print(f"Read numbers from {file_path}")
            print()
            del arr
            del sorted_arr

for i in range(3):
    for j in range(3):
        for k in range(3):
            file_path = f"data/{m[i]}_{n[j]}_{k}.txt"
            arr = read_numbers_from_file(file_path)

            # before_memory_usage = process.memory_info().rss / (1)
            start_time = time.time() * 1000
            tracemalloc.reset_peak()
            sorted_arr = clustered_binary_insertion_sort(arr)
            current, peak = tracemalloc.get_traced_memory()
            end_time = time.time() * 1000
            tracemalloc.reset_peak()
            # after_memory_usage = process.memory_info().rss / (1)
            execution_time = end_time - start_time

            save_numbers_to_file(sorted_arr, f"result/Clustered_Insertion_Sort_{m[i]}_{n[j]}_{k}.txt")

            print("Sorted array using Clustered Binary Insertion Sort")
            print("Execution Time: {:.3f} ms".format(execution_time))
            # print("Memory Usage: {:.6f} B".format(after_memory_usage - before_memory_usage))
            print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
            print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))

            print(f"Read numbers from {file_path}")
            print()
            del arr
            del sorted_arr