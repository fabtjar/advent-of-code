with open('input.txt') as f:
    lines = f.read().splitlines()


def get_rating(func):
    check_lines = lines[:]
    for i in range(len(lines[0]) + 1):
        if len(check_lines) == 1:
            return int(check_lines[0], 2)
        count = len([line for line in check_lines if int(line[i]) == 1])
        mostly = '1' if func(count, check_lines) else '0'
        check_lines = [line for line in check_lines if line[i] == mostly]


oxygen_generator_rating = get_rating(lambda c, l: c >= len(l) / 2)
co2_scrubber_rating = get_rating(lambda c, l: c < len(l) / 2)

print(oxygen_generator_rating * co2_scrubber_rating)
