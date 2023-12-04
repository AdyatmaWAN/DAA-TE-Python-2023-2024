import copy
import tracemalloc
import time
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

values = [0, 1, 6, 7, 8, 12, 13, 14, 19, 20]
tracemalloc.start()
start = time.time()*1000
tracemalloc.reset_peak()
true = findPartition(values, len(values))
current, peak = tracemalloc.get_traced_memory()
end = time.time()*1000
tracemalloc.reset_peak()
if true == True:
    print("Can be divided into two",
          "subsets of equal sum")
else:
    print("Can not be divided into ",
          "two subsets of equal sum")
print()
print("Execution Time: {:.3f} ms".format(end - start))
print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))
