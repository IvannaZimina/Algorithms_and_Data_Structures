# Create a function named counting_sort() that takes a list lst as its parameter.

def counting_sort(lst):
 
   # if list is empty or has one element, return itself 
    
    # find the largest element
    # and create the counting list

    
    # fill the counting list with frequency of each number

    
    # create the sorted output list   


## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
list1 = [int(x) for x in input("Unsorted List: ").split()]

sorted_list = counting_sort(list1)
print(f"Sorted List: {sorted_list}")
