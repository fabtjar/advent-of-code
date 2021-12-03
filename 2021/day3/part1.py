with open('input.txt') as f:
    lines = f.read().splitlines()

bits = [0 for i in lines[0]]

for line in lines:
    for i, bit in enumerate(line):
        if bit == '1':
            bits[i] += 1

bits = ''.join(['1' if b > len(lines) / 2 else '0' for b in bits])
gamma = int(bits, 2)
epsilon = int(''.join(['1' if b == '0' else '0' for b in bits]), 2)

print(gamma * epsilon)
