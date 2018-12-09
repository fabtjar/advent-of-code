rects = []

with open('input.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace(': ', ',')
        line = line.replace('x', ',')
        line = line.split('@ ')[1]
        line = [int(i) for i in line.split(',')]
        rects.append(line)

tile_width = 0
tile_height = 0
for x, y, width, height in rects:
    tile_width = max(tile_width, x + width)
    tile_height = max(tile_height, y + height)

tiles = []
for y in range(tile_height):
    i = []
    for x in range(tile_width):
        i.append(-1)
    tiles.append(i)

for x, y, width, height in rects:
    for hor in range(x, x + width):
        for ver in range(y, y + height):
            tiles[ver][hor] += 1

total_tiles = 0
for y in tiles:
    for x in y:
        if x >= 1:
            total_tiles += 1
print(total_tiles)
