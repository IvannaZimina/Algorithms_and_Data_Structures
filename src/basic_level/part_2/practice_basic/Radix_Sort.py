# Create a function named radix_sort() that takes a list lst as its parameter.

# Replace ___ with your code

# counting sort to sort the elements on the basis of significant places
def counting_sort(lst, place):
    
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]

# function to implement radix sort
def radix_sort(lst):
    # write your code here
    ___

## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
data = list(map(int, input().split()))
radix_sort(data)
print(data)