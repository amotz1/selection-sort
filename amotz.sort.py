

# TODO(aviv): Automate the testing.
# I verified that when I break this function, running amotzsort([9, 4, 9, 2]) fails with an assertion error.
# [amotz] you are right, this function is not relevant and was part
# of my thinking process, i changed the name of the function to preliminarytest
def isSorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


# [aviv] I'm not sure what this function does, but it doesn't sort the input correctly.
# [amotz] this function was part of my thought process and is indeed not relevant.
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


print(isSorted(amotzsort([3, 5, 11, 3, 13])))
print(isSorted(amotzsort([7, 8, 7, 9, 5, 2])))
print(isSorted(amotzsort([6, 8, 8, 5, 4, 3])))
print(isSorted(amotzsort([6, 8, 9, 9, 4, 3])))
print(isSorted(amotzsort([8, 6, 6, 6, 9, 3, 2, 1, 2])))
