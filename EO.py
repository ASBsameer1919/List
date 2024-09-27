'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
Ans
'''
# Function to separate even and odd numbers into two lists
def separate_even_odd(size, elements):
    even_list = []
    odd_list = []
    
    for num in elements:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    return even_list, odd_list

# Input the size of the list
size = int(input("Enter the size of the list: "))

# Input the elements of the list
elements = []
for _ in range(size):
    elements.append(int(input()))

# Get the even and odd lists
even_list, odd_list = separate_even_odd(size, elements)

# Output the results
print("The even list", even_list)
print("The odd list", odd_list)

