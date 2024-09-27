'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
Ans
'''
# Function to find the largest number in a list
def find_largest_number(numbers):
    return max(numbers)

# Input: size of the list
size = int(input("Enter the size of the list: "))

# Input: elements of the list
numbers = []
for _ in range(size):
    num = int(input())
    numbers.append(num)

# Output: largest element in the list
largest_number = find_largest_number(numbers)
print("The largest element is:", largest_number)
