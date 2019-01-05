

# TODO(aviv): Automate the testing.
# I verified that when I break this function, running amotzsort([9, 4, 9, 2]) fails with an assertion error.
def isSorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


# [amotz] (this function is indeed not relevant or used.
def preliminarytest(x):
    print(x)
    count = x[0]
    for i in range(0, len(x)):
        if count > x[i]:
            count = x[i]
    a = 0
    b = x.index(count)
    x[a], x[b] = x[b], x[a]
    count = x[1]
    for i in range(1, len(x)):
        if count > x[i]:
            count = x[i]
    a = 1
    b = x.index(count)
    x[a], x[b] = x[b], x[a]
    count = x[2]
    for i in range(2, len(x)):
        if count > x[i]:
            count = x[i]
    a = 2
    b = x.index(count)
    x[a], x[b] = x[b], x[a]
    # The assertion below fails
    # assert isSorted(x)
    print(x)


# This function is suppose to find a min of arrays
# that reduce in size by 1 each iteration of the for loop
# (so if for example it takes an array [7,8,1] it prints 1
# and then it takes the array [8,1] and it also prints 1  and so on.
# it was also part of my thinking process and is not relevant, i changed the name to findingmintest1
def findingmintest1(x):
    for i1 in range(0, len(x)):
        # [aviv] "count" is not a good name for this variable.
        # [amotz] changed the variable name to findingmin
        findingmin = x[i1]

        for i in range(i1, len(x)):
            if findingmin > x[i]:
                findingmin = x[i]
        print(findingmin)


# This is the actual function and as you can see below, it produce True for various arrays
# that are tested with your function isSorted, i changed the name for amotzsort to reduce confusion
def amotzsort(x):
    # print("the array is=", x)
    for i1 in range(0, len(x)):
        # print("i1=", i1)
        findingmin = x[i1]
        # print("count=", count)
        for i in range(i1, len(x)):
            #  print("i=", i)
            #   print("x[i]=", x[i])
            if findingmin > x[i]:
                findingmin = x[i]
        #        print("x.index(count,i1,len(x))=", x.index(count, i1, len(x)))
        # print("count=", count)
        a = i1
        b = x.index(findingmin, i1, len(x))
        # print("b=", b)
        # print("a=", a)
        x[a], x[b] = x[b], x[a]
        # print("the array is=", x)
    assert isSorted(x)
    return (x)

# This implements "bubble sort"
# Iterate through the array comparing adjacent pairs; in case they're not in order, swap the pair.
# Continue until no pairs need swapping
def bubbleSort(x):
    swapped = True
    while swapped:
        swapped = False
        for i in range (0, max(0, len(x) - 1)):
            j = i + 1
            if x[i] > x[j]:
                temp = x[i]  # type: object
                x[i] = x[j]
                x[j] = temp
                swapped = True
            # print(i, x)

# This function does not sort, rather it just overwrites the input with unrelated sorted values.
# This broken sort currently passes our tests.
# TODO(aviv): Make our tests fail this function.
def brokenSort(x):
    for i in range (0, len(x)):  # type: int
        x[i] = 101 + i


print(isSorted(amotzsort([3, 5, 11, 3, 13])))
print(isSorted(amotzsort([7, 8, 7, 9, 5, 2])))
print(isSorted(amotzsort([6, 8, 8, 5, 4, 3])))
print(isSorted(amotzsort([6, 8, 9, 9, 4, 3])))
print(isSorted(amotzsort([8, 6, 6, 6, 9, 3, 2, 1, 2])))

print("*********************************************************************************************")

# Runs different sort functions (currenly amotsSort and bubbleSort) on several inputs.
# Prints the input and the sorted result.
# Asserts that the result is sorted.
def test1():
    # TODO(aviv): Improve testing. While developing bubbleSort, I had a bug where sorting [1, 2, 3] resulted in
    #  [3, 3, 3]. Just using isSorted did not catch ths bug as the result is sorted but has the wrong elements.
    # One way to achieve this would be to verify that all of our sort functions end up with the same result or maybe
    # just compare to the built-in Python sort(). Doing this will require some restructuring as our sort functions sort
    # in place (that is, they modify the input rather than returning a sorted copy).
    for testFunction in [amotzsort, bubbleSort, brokenSort]:
        print ("testing function: ", testFunction)
        testCases = [[3, 5, 11, 3, 13],
                     [7, 8, 7, 9, 5, 2],
                     [6, 8, 8, 5, 4, 3],
                     [6, 8, 9, 9, 4, 3],
                     [8, 6, 6, 6, 9, 3, 2, 1, 2],
                     # Some boundary cases:
                     [1, 2, 3], # an already sorted list
                     [3, 2, 1], # a list in reverse order
                     [], # empty test case (length 0)
                     [1], # test case of length 1
                     [1, 1, 1]] # test case with all elements equal

        for testCase in testCases:
            print("in\t", testCase)
            testFunction(testCase)
            print("out\t", testCase)
            assert (isSorted(testCase))
            print()

test1()


# This function is just to here demonstrate that amotzsort changes the input and returns a reference (like a "pointer")
# to the input.
def demoInputChanges():
    x = [2, 1, 3]
    print("x=", x)
    print("y = amotzsort(x)")
    y = amotzsort(x)
    print("x=", x)
    print("y=", y)
    y[1] = 17
    print("y[1] = 17")
    print("x=", x)
    print("y=", y)


demoInputChanges()
