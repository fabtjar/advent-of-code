lines = []

with open('input.txt') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

for a in lines:
    for b in lines:
        diff = 0
        letters = ''
        for i in range(len(a)):
            if a[i] == b[i]:
                letters += a[i]
            else:
                diff += 1
        if diff == 1:
            same = letters

print(same)
