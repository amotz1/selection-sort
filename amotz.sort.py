import random
import timeit


# [Aviv] Naming.... Try to use camel case, capital letters, and underscores in a consistent way. I'm not sure
# what the typical Python naming conventions are, but regardless "amotzisSorted" should be "amotzIsSorted"

# [amotz] i read in stackoverflow that the convention in python is to put two underscores before privent functions so i changed the name of the privet functions
# and changed the name of Quicksort to quicksort
def __swap(list, index1, index2):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp
    return list


def __partition(list, start, end):
    pivot = end
    pindex = start
    for i in range(pindex, pivot):
        if list[i] < list[pivot]:
            __swap(list, i, pindex)
            pindex = pindex + 1
    __swap(list, pindex, pivot)
    return pindex


def __quicksort(list, start, end):
    if start >= end:
        return list
    pindex = __partition(list, start, end)
    __quicksort(list, start, pindex - 1)
    __quicksort(list, pindex + 1, end)
    return list


# [Aviv] It's bad form to have 2 functions that differ only by case (quicksort, Quicksort). I think that both could be
# named "quicksort". If one of them needs to have a strange name, then make that the private one, not the one that
# would typically be used by users.

# changed the name of Quicksort to quicksort
def quicksort(list):
    __quicksort(list, 0, len(list) - 1)
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


# [aviv] This function name is not good. This function tests that a supplied test function sorts a supplied list
# correctly. If it's too difficult to name this function, then it might not be a good function.
# I'd rename it to: testSortFunctionOnList(sortFunction, list)

# [amotz] i read in stuck overflow that the convention of functions in python is to separate words with underscore
# and use lower case letters,
# so i changed the name of the function according to what you said and stackoverflow said.
def test_sort_function_on_list(sort_function, list):
    copyoflist = copy_of_list(list)
    sort_function(list)
    if sorted(copyoflist) == list:
        return True
    else:
        return False


# [amotz] this function doesn't take any arguments, it make test cases to check if our functions sort them correctly.
# it uses a loop over all the test cases and all our test functions and check if the functions that suppose to work work.
def testing_sort_functions():
    testcases = [[3, 2, 1],
                 [4, 4],
                 [4, 5, 6],
                 [],
                 [1, 1],
                 [3, 5, 11, 3, 13],
                 [7, 8, 7, 9, 5, 2],
                 [6, 8, 8, 5, 4, 3],
                 [8, 6, 6, 6, 9, 3, 2, 1, 2]]
    sortfunctions = [amotzsort, bubbleSort, quicksort]
    for testcase in testcases:
        for sortfunction in sortfunctions:
            assert (test_sort_function_on_list(sortfunction, testcase) == True)


testing_sort_functions()


# [amotz] this function will take no arguments but will return a list with 2000 elements from 1 to 100,000.
# it will produce an empty list and put it in a variable called large_list.
# then i will use a while loop with a condition that until the length of the list< 2000 we will append a number to the list using
# generating_random_number. at the end of the process we will return large_list with 2000  numbers
def generating_big_list():
    large_list = []
    while len(large_list) < 2000:
        large_list.append(generating_random_number())
    return large_list


# [amotz] this function takes no parameters, it checking if the list is indeed of 2000 items by checking if the length of the list is of 2000 elements
def test_generating_big_list():
    assert (len(generating_big_list()) == 2000)


# [amotz] generate random number from 1 to 10000 by calling random.randrange method from the library random and put it in a variable random_number
def generating_random_number():
    random_number = random.randrange(1, 100001)
    return random_number


test_generating_big_list()


# [amotz] this function sum all elements in a list and then devide by the number of elements on the list. it do so by making a sum variable that is initialized to 0, and then using a for loop to go through each element in the list and increment sum each iteration by the item in the list
# it then returns the sum devided by the length of the list
def average_of_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum / len(list)


def test_average_of_list():
    testcases = [[5, 10, 15], [20, 30, 40, 60], [3, 3, 3]]
    for testcase in testcases:
        print('in', testcase, 'out', average_of_list(testcase))


test_average_of_list()


# [amotz] this is the time measurement function, it takes no arguments. it will use two while loops with two separate counters.
# in the inner loop we will make 10 time measurements with each sort function on a list with 2000 elements.
# in the outer loop we will make the average of 10 measurements of each sort function with the helper function average_of_list
# and append it to a list with the name of each sort function.
# we will then return a list with the name of the sort function and the average of 10 time measurments of that sort function on a list with 2000 elements.
def time_measurment_test():
    sort_functions = [amotzsort, bubbleSort, quicksort]
    count = 0
    results1 = []
    while count < 3:
        count1 = 0
        results = []
        while count1 < 10:
            large_list = generating_big_list()
            start = timeit.default_timer()
            sort_functions[count](large_list)
            time = timeit.default_timer() - start
            results.append(time)
            count1 = count1 + 1
        results1.append(sort_functions[count].__name__ + ' ' + str(average_of_list(results)))
        count = count + 1
    return results1


print(time_measurment_test())
