input_text = open('input.txt', 'r').read()
frequencies = input_text.split('\n')

current_frequency = 0
used_frequency = [current_frequency]
reached_twice = None

while not reached_twice:
    for frequency in frequencies[:-1]:
        number = int(frequency[1:])
        
        if frequency[0] is "+":
            current_frequency += number
        else:
            current_frequency -= number
            
        if current_frequency in used_frequency:
            reached_twice = current_frequency
            break
            
        used_frequency.append(current_frequency)
        print(frequency)

print(reached_twice)
