# The logic with angled lines crossing is incorrect.

def parse_data(lines):
    points = []
    for line in lines:
        a, b = line.split('->')
        x1, y1 = a.split(',')
        x2, y2 = b.split(',')
        x1, y1, x2, y2 = (int(p) for p in (x1, y1, x2, y2))

        if x2 < x1:
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


def get_min_max_bounds(line):
    x1, y1, x2, y2 = line
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def get_bounds_overlap(a, b):
    a = get_min_max_bounds(a)
    b = get_min_max_bounds(b)

    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    return ax1 <= bx2 and ax2 >= bx1 and ay1 <= by2 and ay2 >= by1


def get_overlap_points(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    if not get_bounds_overlap(a, b):
        return None

    is_a_angle = ax1 != ax2 and ay1 != ay2
    is_b_angle = bx1 != bx2 and by1 != by2

    # Both hor/ver lines.
    if not is_a_angle and not is_b_angle:
        x1 = max(ax1, bx1)
        x2 = min(ax2, bx2)
        y1 = max(ay1, by1)
        y2 = min(ay2, by2)
        return get_sub_points(x1, y1, x2, y2)

    # One of each.
    if not is_a_angle or not is_b_angle:
        # Angle = a; Line = b.
        if is_b_angle:
            ax1, ay1, ax2, ay2 = bx1, by1, bx2, by2
        x = ax1 + abs(by1 - ay1)
        if bx1 <= x <= bx2:
            return [(x, by1, x, by1)]

    # Angles line up if distance x/y is equal.
    if sign(ax1 - bx1) == sign(ay1 - by1):
        x1, y1 = max(ax1, bx1), max(ay1, by1)
        x2, y2 = min(ax2, bx2), min(ay2, by2)
        return [(x1, y1, x2, y2)]

    # Angles can't cross if their x/y odd/even don't match.
    if (ax1 % 2 == ay1 % 2) != (bx1 % 2 == by1 % 2):
        return None

    d = abs(by1 - ay1) // 2
    x, y = ax1 + d, ay1 + d
    dx, dy = x - bx1, y - by1
    if sign(dx) == sign(bx2 - bx1) and sign(dy) == sign(by2 - by1):
        return [(x, y, x, y)]


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
