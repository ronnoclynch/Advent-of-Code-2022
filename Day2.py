## Advent of Code Day 2 
# Part 1 - Answer = 15523


# Get Data 
with open("RPS.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# Part 1 - - - - - - - - - - - - - - - - - - -

# Dictionary
result_p1 = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

total_points_p1 = 0
for round in rounds:
    total_points_p1 += result_p1[round]

# print part 1 answer
print("Total Score = ", total_points_p1)

# Part 2 - - - - - - - - - - - - - - - - - - -

results_p2 = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

total_points_p2 = 0
for round in rounds:
    total_points_p2 += results_p2[round]

# print part 2 answer
print("Total Score = ", total_points_p2)


