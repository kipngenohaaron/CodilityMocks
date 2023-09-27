def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    
    # Find the least common multiple (LCM) of all elements in a
    lcm_a = a[0]
    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])
    
    # Find the greatest common divisor (GCD) of all elements in b
    gcd_b = b[0]
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])
    
    count = 0
    multiple = lcm_a
    
    # Check multiples of LCM of a until it's less than or equal to GCD of b
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    
    return count

# Input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function to get the count of integers between the sets
result = getTotalX(a, b)

# Output the result
print(result)
