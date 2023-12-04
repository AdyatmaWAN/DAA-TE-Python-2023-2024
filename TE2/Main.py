import random
import time
import os
import tracemalloc
import copy

# Partition the values with those before index start_index fixed.
# test_assignment is the test assignment so far.
# test_value = total value of the first set in test_assignment.
# Initially best assignment and its error are in
#     best_assignment and best_err.
# Update those to reflect any improved solution we find.
def branchAndBound(values, startIndex, totalValue, unassignedValue, testAssigment, testValue, bestAssigment, bestErr):
    # If start_index is beyond the end of the array,
    # then all entries have been assigned.
    # print(startIndex)
    if startIndex >= len(values):
        # We're done. See if this assignment is better than
        # what we have so far.
        testErr = abs(2 * testValue - totalValue)
        if testErr < bestErr[0]:
            # This is an improvement. Save it.
            bestErr[0] = testErr
            bestAssigment = copy.deepcopy(testAssigment)
            # print(bestAssigment)
            # print(bestErr)
    else:
        # See if there's any way we can assign
        # the remaining items to improve the solution.
        testErr = abs(2 * testValue - totalValue)
        # print(testErr, unassignedValue, bestErr[0])
        # print(testErr - unassignedValue, bestErr[0])
        if testErr - unassignedValue < bestErr[0] and bestErr[0] != 0:
            # print("here")
            # There's a chance we can make an improvement.
            # We will now assign the next item.

            # Try adding values[start_index] to set 1.
            unassignedValue -= values[startIndex]
            testAssigment[startIndex] = True
            branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                           testAssigment, testValue + values[startIndex],
                           bestAssigment, bestErr)
            #false unassigned value should be added back
            unassignedValue += values[startIndex]

            # Try adding values[start_index] to set 2.
            testAssigment[startIndex] = False
            branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                           testAssigment, testValue, bestAssigment,
                           bestErr)

# Dynamic Programming based python
# program to partition problem
# Returns true if arr[] can be
# partitioned in two subsets of
# equal sum, otherwise false
def findPartition(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    return part[sum // 2][n]
    # This code is contributed
    # by mohit kumar 29

def generate_random_numbers(n):
    numbers = set()
    max = n
    while len(numbers) < n:
        num = random.randint(0, max-1)
        numbers.add(num)
        num = max*2 - num
        numbers.add(num)
    return list(numbers)

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

def generate(num):
    for j in range(3):
        random_numbers = generate_random_numbers(num)
        # Save random, sorted, and reverse sorted numbers to text files
        save_numbers_to_file(random_numbers, f'data/random_numbers_{num}_{j}.txt')

if __name__ == '__main__':

    n = [10, 40, 80]
    # n = [10]
    ## Generate random numbers
    ## un comment to generate random numbers
    # for i in n:
    #     generate(i)

    ## Read random numbers from file

    tracemalloc.start()

    # Driver Code
    for i in n:
        for j in range(3):
            file_path = f"data/random_numbers_{i}_{j}.txt"
            arr = read_numbers_from_file(file_path)

            print(f"Read numbers from {file_path}")
            print(arr)
            print()

            start = time.time()*1000
            tracemalloc.reset_peak()
            true = findPartition(arr, len(arr))
            current, peak = tracemalloc.get_traced_memory()
            end = time.time()*1000
            tracemalloc.reset_peak()

            print(f"Read numbers from {file_path}")
            print("Divided using Dynamic Programming")
            print("Execution Time: {:.3f} ms".format(end - start))
            print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
            print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))
            # Function call
            if true == True:
                print("Can be divided into two",
                      "subsets of equal sum")
            else:
                print("Can not be divided into ",
                      "two subsets of equal sum")
            print()

            del true

            # Example usage:
            values = arr
            start_index = 0
            total_value = sum(values)
            unassigned_value = total_value
            test_assignment = [False] * len(values)
            test_value = 0
            best_assignment = [False] * len(values)
            best_err = [float('inf')]  # Using a list to mimic pass-by-reference for best_err

            start = time.time()*1000
            tracemalloc.reset_peak()
            branchAndBound(values, start_index, total_value, unassigned_value,
                           test_assignment, test_value,
                           best_assignment, best_err)
            current, peak = tracemalloc.get_traced_memory()
            end = time.time()*1000
            tracemalloc.reset_peak()

            print(f"Read numbers from {file_path}")
            print("Divided using Branch and Bound")
            print("Execution Time: {:.3f} ms".format(end - start))
            print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
            print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))
            print("Best error:", best_err)
            print()
            print()

            del values
            del start_index
            del total_value
            del unassigned_value
            del test_assignment
            del test_value
            del best_assignment
            del best_err