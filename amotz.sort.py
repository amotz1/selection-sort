x = [12, 9, 3, 8]


def amotzsort(x):
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
    print(x)


amotzsort([3, 1, 1, 3])


def findingmax(x):
    for i1 in range(0, len(x)):
        count = x[i1]
        for i in range(i1, len(x)):
            if count > x[i]:
                count = x[i]
        print(count)


findingmax([15, 81, 32, 78])


def sortinglist(x):
    print("the array is=", x)
    for i1 in range(0, len(x)):
        print("i1=", i1)
        count = x[i1]
        print("count=", count)
        for i in range(i1, len(x)):
            print("i=", i)
            print("x[i]=", x[i])
            if count > x[i]:
                count = x[i]
                print("x.index(count,i1,len(x))=", x.index(count, i1, len(x)))
        print("count=", count)
        a = i1
        b = x.index(count, i1, len(x))
        print("b=", b)
        print("a=", a)
        x[a], x[b] = x[b], x[a]
        print("the array is=", x)
    return (x)


print(sortinglist([3, 1, 8, 9, 8, 23, 1, 34, 67, 67, 89, 23]))
