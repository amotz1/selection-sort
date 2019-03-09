import random
import timeit


# It's bad form to have constants in the code.
NUM_TESTS = 27
TEST_SIZE = 1000000 # TODO

# I suspect that this is actually a list, not an array. Regardless you should name this variable not just based on its
# type but rather on its semantics. Name it "timeMeasurements".
array = []
for i in range(NUM_TESTS):
    # [aviv] Either use constants or just test over the entire range of integers.
    y = ([random.randrange(1, 4), random.randrange(1, 4), random.randrange(1, 4)])
    print("the random array to be sorted is", y)
    # [aviv] You call sorted(..) here for the first time.
    print("the sorted array is", sorted(y))
    start = timeit.default_timer()
    # [aviv] You now measure sorted, but this is the second call, and so it will be faster due to caching.
    sorted(y)
    time = timeit.default_timer() - start
    array.append(time)
    # [aviv] This is not a correct test, and it would not work when we get to sorting a list of length 1,000,000.
    # I'd just remove it and test correctness correctly somewhere else.
    # [aviv] You call sorted(..) 3 times here. It's wasteful and bad form. (But I've recommended that you remove this
    # anyway.)
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
