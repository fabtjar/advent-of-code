with open('input.txt') as f:
    lines = [(line.split()[0], int(line.split()[1])) for line in f]

aim = 0
hor = 0
depth = 0

for direction, amount in lines:
    if direction == 'forward':
        hor += amount
        depth += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount

print(hor * depth)
