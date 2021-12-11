def parse_data(lines):
    points = []
    for line in lines:
        line = line.split('->')
        x1, y1 = line[0].split(',')
        x2, y2 = line[1].split(',')
        x1, y1, x2, y2 = (int(p) for p in (x1, y1, x2, y2))

        if x1 != x2 and y1 != y2:
            continue

        if x2 < x1 or y2 < y1:
            points.append([x2, y2, x1, y1])
        else:
            points.append([x1, y1, x2, y2])
    return points


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def get_sub_points(x1, y1, x2, y2):
    points = []
    dx = sign(x2 - x1)
    dy = sign(y2 - y1)
    while (x1, y1) != (x2, y2):
        points.append((x1, y1))
        x1 += dx
        y1 += dy
    points.append((x1, y1))
    return points


def get_overlap_points(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    overlaps = ax1 <= bx2 and ax2 >= bx1 and ay1 <= by2 and ay2 >= by1

    if not overlaps:
        return None

    x1 = max(ax1, bx1)
    x2 = min(ax2, bx2)
    y1 = max(ay1, by1)
    y2 = min(ay2, by2)

    return get_sub_points(x1, y1, x2, y2)


def calculate(lines):
    points = parse_data(lines)

    size = len(points)
    overlaps = []
    for i in range(size):
        for j in range(i + 1, size):
            sub_points = get_overlap_points(points[i], points[j])
            if sub_points:
                overlaps += sub_points
    return len(set(overlaps))


with open('input.txt') as f:
    print(calculate(f.read().splitlines()))
