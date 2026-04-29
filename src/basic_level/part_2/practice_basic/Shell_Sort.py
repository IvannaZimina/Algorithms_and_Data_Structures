# Create a function named shell_sort() that takes a list lst as its parameter.

# Replace ___ with your code

def insertion_sort(lst, interval):
    for i in range(interval, len(lst)):
        key = lst[i]            
        j = i - interval          
        while j >= 0 and key < lst[j]:
            lst[j + interval] = lst[j]
            j = j - interval    
        lst[j + interval] = key

def shell_sort(n):
    # write your code here
    ___


## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
data = list(map(int, input().split()))
size = len(lst)

# function call
shell_sort(size)
print(lst)