### Advent of Code Day 1 ### 
# Part 1 - Answer = 70296
# Part 2 - Answer = 

# Getting data 
with open("AoC_Day1.txt") as file:
    data = [i for i in file.read().strip().split("\n")]


# Traversing every STRING in the data 
max = 0
max2 = 0 # Elf with second greatest calories
max3 = 0 # Elf with third greatest calories
count = 0

for item in data:
    if item == '':
        count = 0   # resetting the count
    else: 
        num = int(item) 
        count += num 
    
    # Saving the maximum calories
    if count > max:
        max3 = max2
        max2 = max 
        max = count 
    elif count > max2:
        max3 = max2
        max2 = count 
    elif count > max3:
        max3 = count 


print("Answer to part 1:", max) 
print("Answer to part 2:", max+max2+max3)
