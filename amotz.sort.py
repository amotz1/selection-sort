# [amotz new] hey! i did some new things:
# 1) i added quicksort project here so we can test it with our functions and added a new function Quicksort that takes a list and sort it in place with our quicksort function.
# 2) i made a new function called copy_of_list that make a copy of a list that is given to it as an argument. i also made a function to test this function name test_copy
# 3) i changed amotzisSorted so it is now failing your brokensort test and successfully test all our sorting test functions except mergesort that i still didnt work with yet.
# 4) i made  a function that test the amotzisSorted function name test_amotzisSorted.


def swap(list, index1, index2):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp
    return list


def partition(list, start, end):
    pivot = end
    pindex = start
    for i in range(pindex, pivot):
        if list[i] < list[pivot]:
            swap(list, i, pindex)
            pindex = pindex + 1
    swap(list, pindex, pivot)
    return pindex


def quicksort(list, start, end):
    if start >= end:
        return list
    pindex = partition(list, start, end)
    quicksort(list, start, pindex - 1)
    quicksort(list, pindex + 1, end)
    return list


# [amotz] this function take a list and use quicksort function with a list and 0 and len(list)-1 as arguments for convinience of use
def Quicksort(list):
    quicksort(list, 0, len(list) - 1)
    return list


def amotzsort(list):
    for i1 in range(0, len(list)):
        findingmin = list[i1]
        for i in range(i1, len(list)):
            if findingmin > list[i]:
                findingmin = list[i]
        a = i1
        b = list.index(findingmin, i1, len(list))
        list[a], list[b] = list[b], list[a]
    return list


# This implements "bubble sort"
# Iterate through the array comparing adjacent pairs; in case they're not in order, swap the pair.
# Continue until no pairs need swapping
def bubbleSort(x):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, max(0, len(x) - 1)):
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
    for i in range(0, len(x)):  # type: int
        x[i] = 101 + i
    return x


# [amotz] copy_of_list takes a list as an argument and return a copy of the list. first it creates a list with the same number of empty elements as the argument list.
# then it will make a loop that appends to the empty list for each element the element in the original list that was given to the function as an argument.
# it then will  return the new list
def copy_of_list(list):
    new_list = [None] * len(list)
    for element in range(len(new_list)):
        new_list[element] = list[element]
    return new_list


# [amotz] this function test the copy_of_list function, it create testcases and loop over them to check wether the copy of the testcase is equal the original testcase.
def test_copy():
    testcases = [[], [1, 2, 3], [1]]
    for testcase in testcases:
        assert (copy_of_list(testcase) == testcase)


test_copy()


# [amotz]  amotzisSOrted takes  a list as an argument make a copy of the list with the use of the function copy_of_list and put the copy in a variable name copyoflist.
# then it use a testfunction to sort the list and check if sorting the copy of our list with python sort gives the same results as our test function on the original list.
# if it produce the same results it returns True and if its not it returns False.
def amotzisSorted(list, test_function):
    copyoflist = copy_of_list(list)
    test_function(list)
    if sorted(copyoflist) == list:
        return True
    else:
        return False


# [amotz] this function does't take any arguments, it make test cases for amotzisSorted and check if all our test functions are correct.
# it use a loop over all the test cases and all our test functions and check if the functions that suppose to work work and that brokensort is indeed broken.
def test_amotzisSorted():
    testcases = [[3, 2, 1], [4, 4], [4, 5, 6]]
    testfunctions = [amotzsort, bubbleSort, Quicksort]
    for testcase in testcases:
        for testfunction in testfunctions:
            assert (amotzisSorted(testcase, testfunction) == True)
    testfunction = brokenSort
    for testcase in testcases:
        assert (amotzisSorted(testcase, testfunction) == False)


test_amotzisSorted()
print("*********************************************************************************************")

# Runs different sort functions (currenly amotsSort and bubbleSort) on several inputs.
# Prints the input and the sorted result.
# Asserts that the result is sorted.
# def test1():
# TODO(aviv): Improve testing. While developing bubbleSort, I had a bug where sorting [1, 2, 3] resulted in
#  [3, 3, 3]. Just using isSorted did not catch ths bug as the result is sorted but has the wrong elements.
# One way to achieve this would be to verify that all of our sort functions end up with the same result or maybe
# just compare to the built-in Python sort(). Doing this will require some restructuring as our sort functions sort
# in place (that is, they modify the input rather than returning a sorted copy).
for testFunction in [amotzsort, bubbleSort, Quicksort]:
    print("testing function: ", testFunction)
    testCases = [[3, 5, 11, 3, 13],
                 [7, 8, 7, 9, 5, 2],
                 [6, 8, 8, 5, 4, 3],
                 [6, 8, 9, 9, 4, 3],
                 [8, 6, 6, 6, 9, 3, 2, 1, 2],
                 # Some boundary cases:
                 [1, 2, 3],  # an already sorted list
                 [3, 2, 1],  # a list in reverse order
                 [1],
                 [],
                 [1, 1]]  # test case of length 1

    for testCase in testCases:
        assert (amotzisSorted(testCase, testFunction))
        #       new_list1 = copy_of_list(testCase)
        print("in\t", testCase)
        testFunction(testCase)
        print("out\t", testCase)

# This function is just to here demonstrate that amotzsort changes the input and returns a reference (like a "pointer")
# to the input.
# TODO(amotz): Feel invited to delete this function after you feel like you understand what's going on here.
# def demoInputChanges():
#    x = [2, 1, 3]
#    print("x=", x)
#    print("y = amotzsort(x)")
#    y = amotzsort(x)
#    print("x=", x)
#    print("y=", y)
#    y[1] = 17
#    print("y[1] = 17")
#    print("x=", x)
#    print("y=", y)


# demoInputChanges()
