import copy

def branchAndBound(values, startIndex, totalValue, unassignedValue, testAssigment, testValue, bestAssigment, bestErr):
    if testAssigment[0] == True and testAssigment[1] == True and testAssigment[2] == False:
        print("here")
    # print(testAssigment)
    if startIndex >= len(values):
        testErr = abs(2 * testValue - totalValue)
        if testErr < bestErr[0]:
            bestErr[0] = testErr
            bestAssigment[:] = testAssigment[:]  # Use list slicing for a copy
            print("be", bestErr)

    else:
        testErr = abs(2 * testValue - totalValue)
        if testErr - unassignedValue < bestErr[0] and bestErr[0] != 0:
            testAssigment[startIndex] = False
            if testAssigment[0] == True and testAssigment[1] == True and testAssigment[2] == False:
                print("here false")
                print("false branch", testAssigment)
                testErr = abs(2 * testValue - totalValue)
                print("testErr", testErr)
                print("unassignedValue", unassignedValue)
                print(testErr - unassignedValue, bestErr[0])
                branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                               testAssigment, testValue, bestAssigment,
                               bestErr)

            unassignedValue -= values[startIndex]
            testAssigment[startIndex] = True
            if testAssigment[0] == True and testAssigment[1] == True and testAssigment[2] == False:
                print("here true")
                print("true branch", testAssigment)
            branchAndBound(values, startIndex + 1, totalValue, unassignedValue,
                           testAssigment, testValue + values[startIndex],
                           bestAssigment, bestErr)


values = [0, 1, 6, 7, 8, 12, 13, 14, 19, 20]
totalValue = sum(values)
unassignedValue = totalValue
testAssigment = [False] * len(values)
bestAssigment = [False] * len(values)
bestErr = [float('inf')]

branchAndBound(values, 0, totalValue, unassignedValue, testAssigment, 0, bestAssigment, bestErr)

set1 = [values[i] for i in range(len(values)) if bestAssigment[i]]
set2 = [values[i] for i in range(len(values)) if not bestAssigment[i]]

print("Set 1:", set1)
print("Set 2:", set2)
