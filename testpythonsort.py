import random
import timeit
array = []
for i in range(27):
    y = ([random.randrange(1, 4), random.randrange(1, 4), random.randrange(1, 4)])
    print("the random array to be sorted is", y)
    print("the sorted array is", sorted(y))
    start = timeit.default_timer()
    sorted(y)
    time = timeit.default_timer() - start
    array.append(time)
    if sorted(y)[0] <= sorted(y)[1] <= sorted(y)[2]:
        print("you got it")
print("the maximum time is", max(array))
print("the minimum time is", min(array))
sum1 = 0
length= len(array)
for i in range(len(array)):
    sum1 = sum1 + array[i]
average = sum1/len(array)
print("the average time is", average)
