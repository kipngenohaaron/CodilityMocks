def kangaroo(x1, v1, x2, v2):
    # Check if the kangaroos have the same initial position and jump distance.
    if x1 == x2 and v1 == v2:
        return "YES"
    # Check if the kangaroos have the same jump distance but different initial positions.
    elif v1 == v2 and x1 != x2:
        return "NO"
    # Check if the kangaroos can reach the same location at the same time.
    elif (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) >= 0:
        return "YES"
    else:
        return "NO"

# Input
x1, v1, x2, v2 = map(int, input().split())

# Call the function to check if kangaroos meet
result = kangaroo(x1, v1, x2, v2)

# Output the result
print(result)
def kangaroo(x1, v1, x2, v2):
    # Check if the kangaroos have the same initial position and jump distance.
    if x1 == x2 and v1 == v2:
        return "YES"
    # Check if the kangaroos have the same jump distance but different initial positions.
    elif v1 == v2 and x1 != x2:
        return "NO"
    # Check if the kangaroos can reach the same location at the same time.
    elif (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) >= 0:
        return "YES"
    else:
        return "NO"

# Input
x1, v1, x2, v2 = map(int, input().split())

# Call the function to check if kangaroos meet
result = kangaroo(x1, v1, x2, v2)

# Output the result
print(result)
