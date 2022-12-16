with open("input.txt") as f:
    lines = f.readlines()

max_calories = 0
calories = 0

for line in lines:
    if line == "\n":
        max_calories = max(max_calories, calories)
        calories = 0
        continue
    calories += int(line)

print(max_calories)
