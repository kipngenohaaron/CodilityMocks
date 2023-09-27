def breakingRecords(scores):
    # Initialize variables to keep track of highest and lowest scores
    highest_score = scores[0]
    lowest_score = scores[0]

    # Initialize counters for breaking records
    highest_count = 0
    lowest_count = 0

    # Iterate through the scores starting from the second game (index 1)
    for score in scores[1:]:
        if score > highest_score:
            highest_score = score
            highest_count += 1
        elif score < lowest_score:
            lowest_score = score
            lowest_count += 1

    return [highest_count, lowest_count]

# Input
n = int(input().strip())
scores = list(map(int, input().strip().split()))

# Call the function to calculate record-breaking counts
result = breakingRecords(scores)

# Output the result
print(result[0], result[1])
