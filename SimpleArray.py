def simpleArraySum(ar):
    # Initialize a variable to store the sum
    total = 0
    
    # Iterate through the elements in the array and add them to the total
    for num in ar:
        total += num
    
    return total

# Input
n = int(input().strip())  # The size of the array
ar = list(map(int, input().strip().split()))  # The array elements

# Call the function to calculate the sum of the array elements
result = simpleArraySum(ar)

# Output the result
print(result)
