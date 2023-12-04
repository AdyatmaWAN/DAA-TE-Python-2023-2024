import copy
import tracemalloc
import time
def branchAndBound(values, startIndex, totalValue, unassignedValue, testAssigment, testValue, bestAssigment, bestErr):
    # print(testAssigment)
    if startIndex >= len(values):
        testErr = abs(2 * testValue - totalValue)
        if testErr < bestErr[0]:
            bestErr[0] = testErr
            bestAssigment[:] = testAssigment[:]  # Use list slicing for a copy

    else:
        testErr = abs(2 * testValue - totalValue)
        if testErr - unassignedValue < bestErr[0] and bestErr[0] != 0:
            testAssigment[startIndex] = False

            branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                           testAssigment, testValue, bestAssigment,
                           bestErr)

            unassignedValue -= values[startIndex]
            testAssigment[startIndex] = True

            branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                           testAssigment, testValue + values[startIndex],
                           bestAssigment, bestErr)


values = [0, 1, 6, 7, 8, 12, 13, 14, 19, 20]
totalValue = sum(values)
unassignedValue = totalValue
testAssigment = [False] * len(values)
bestAssigment = [False] * len(values)
bestErr = [float('inf')]

tracemalloc.start()
start = time.time()*1000
tracemalloc.reset_peak()
branchAndBound(values, 0, totalValue, unassignedValue, testAssigment, 0, bestAssigment, bestErr)
current, peak = tracemalloc.get_traced_memory()
end = time.time()*1000
tracemalloc.reset_peak()

set1 = [values[i] for i in range(len(values)) if bestAssigment[i]]
set2 = [values[i] for i in range(len(values)) if not bestAssigment[i]]

print("Set 1:", set1, "total:", sum(set1))
print("Set 2:", set2, "total:", sum(set2))
print("Execution Time: {:.3f} ms".format(end - start))
print("Current Memory: {:.3f} KB (Tracemalloc)".format(current / 1024))
print("Peak Memory: {:.3f} KB (Tracemalloc)".format(peak / 1024))