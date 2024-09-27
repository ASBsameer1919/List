'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
# Read the list elements from the first line of input
list_elements = input("Enter the list elements: ").split()

# Convert the list elements to integers
list_elements = [int(element) for element in list_elements]

# Read the value to count from the second line of input
value_to_count = int(input("Enter the value to count: "))

# Count the occurrences of the value in the list
count = list_elements.count(value_to_count)

# Print the count
print(count)
