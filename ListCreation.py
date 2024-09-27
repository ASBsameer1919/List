'''
List
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]
Ans
'''
# Function to create and display the list
def create_and_display_list():
    # Read the size of the list
    n = int(input("Enter the size of the list: "))
    
    # Initialize an empty list
    lst = []
    
    # Read the elements of the list
    for _ in range(n):
        element = int(input())
        lst.append(element)
    
    # Display the list
    print(lst)

# Call the function
create_and_display_list()
