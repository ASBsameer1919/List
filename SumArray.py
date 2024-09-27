'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
Ans
'''
# Function to calculate the sum and mean of array elements
def calculate_mean():
    # Read the number of elements
    n = int(input())
    
    # Initialize the array
    array = []
    
    # Read the elements of the array
    for _ in range(n):
        array.append(int(input()))
    
    # Calculate the sum of the elements
    total_sum = sum(array)
    
    # Calculate the mean
    mean = total_sum / n
    
    # Print the sum and mean
    print(f"{total_sum:.1f}")

# Call the function
calculate_mean()
