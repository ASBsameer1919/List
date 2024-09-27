'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
# Function to reverse the list
def reverse_list(lst):
    return lst[::-1]

# Sample Input
input_list = [10, 20, 30, 40, 50]

# Reversing the list
reversed_list = reverse_list(input_list)

# Printing the reversed list
print("Reversed List:", reversed_list)
