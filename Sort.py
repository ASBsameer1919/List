'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''
# Function to sort the list
def sort_list(lst):
    return sorted(lst)

# Sample Input
input_list = [30, 20, 10, 50, 40]

# Sorting the list
sorted_list = sort_list(input_list)

# Printing the sorted list
print("Sorted List:", sorted_list)
