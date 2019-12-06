with open('input.txt') as f:
    program = [int(x) for x in f.read().split(',')]

program[1] = 12
program[2] = 2

current_pos = 0
running = True

while running:
    opcode, pos1, pos2, pos3 = program[current_pos:current_pos + 4]
    if opcode == 99:
        running = False
    elif opcode == 1:
        program[pos3] = program[pos1] + program[pos2]
    elif opcode == 2:
        program[pos3] = program[pos1] * program[pos2]
    current_pos += 4

print(program[0])
