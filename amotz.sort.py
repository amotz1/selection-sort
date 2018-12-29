x=[12,9,3,8]

# Test change by Yotam made online at github.com

def amotzsort (x):
    print(x)
    count = x[0]
    for i in range (0,len(x)):
        if count>x[i]:
            count=x[i]
    a=0
    b=x.index(count)
    x[a],x[b]=x[b],x[a]
    count=x[1]
    for i in range (1,len(x)):
        if count>x[i]:
            count=x[i]
    a = 1
    b = x.index(count)
    x[a], x[b] = x[b], x[a]
    count=x[2]
    for i in range (2,len(x)):
        if count>x[i]:
            count=x[i]
    a = 2
    b = x.index(count)
    x[a], x[b] = x[b], x[a]
    print(x)
amotzsort([9,4,9,2])
def findingmax (x):
    for i1 in range (0,len(x)):
        count=x[i1]
        for i in range (i1,len(x)):
            if count>x[i]:
                count=x[i]
        print (count)
findingmax([15,81,32,78])

def sortinglist (x):
    for i1 in range (0,len(x)):
        count=x[i1]
        for i in range (i1,len(x)):
            if count>x[i]:
                count=x[i]
        a = i1
        b = x.index(count)
        print (a)
        print(b)
        x[a], x[b] = x[b], x[a]
    return (x)
print(sortinglist([3,1,1]))
