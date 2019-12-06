with open('input.txt') as f:
    first_program = [int(x) for x in f.read().split(',')]


def calculate_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    
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
    
    return program[0]


for n in range(0, 99):
    for v in range(0, 99):
        if calculate_program(first_program[:], n, v) == 19690720:
            print(100 * n + v)
            exit()
