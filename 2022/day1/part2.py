with open("input.txt") as f:
    lines = f.readlines()

calories = [0]

for line in lines:
    if line == "\n":
        calories.append(0)
        continue
    calories[-1] += int(line)

calories.sort()
print(sum(calories[-3:]))
