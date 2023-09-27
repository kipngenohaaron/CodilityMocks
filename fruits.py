def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for apple_distance in apples:
        apple_position = a + apple_distance
        if s <= apple_position <= t:
            apple_count += 1

    for orange_distance in oranges:
        orange_position = b + orange_distance
        if s <= orange_position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)

# Input
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

# Call the function to count apples and oranges
countApplesAndOranges(s, t, a, b, apples, oranges)
