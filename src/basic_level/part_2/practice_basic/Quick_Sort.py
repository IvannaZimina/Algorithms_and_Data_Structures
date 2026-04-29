def quick_sort(lst):


## This input required for testing
# If you want to test you code you can enter data in the following format:
# 1 2 3 4 5
list1 = [int(x) for x in input("Unsorted List: ").split()]

sorted_list = quick_sort(list1)
print(f"Sorted List: {sorted_list}")
