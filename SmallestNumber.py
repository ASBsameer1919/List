'''
Write a Python Program to find the smallest number in a list
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
1
Ans
'''
# Function to find the smallest number in a list
def find_smallest_number(lst):
    return min(lst)

# Main code
if __name__ == "__main__":
    # Input the size of the list
    size = int(input("Enter the size of the list: "))
    
    # Input the elements of the list
    lst = []
    for _ in range(size):
        element = int(input())
        lst.append(element)
    
    # Find and print the smallest number in the list
    smallest_number = find_smallest_number(lst)
    print("Smallest number in the list is:", smallest_number)
