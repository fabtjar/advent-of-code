with open('input.txt') as f:
    lines = [(line.split()[0], int(line.split()[1])) for line in f]

hor = 0
depth = 0

for direction, amount in lines:
    if direction == 'forward':
        hor += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount

print(hor * depth)
