input_text = open('input.txt', 'r').read()
frequencies = input_text.split('\n')

current_frequency = 0

for frequency in frequencies[:-1]:
    number = int(frequency[1:])
    
    if frequency[0] is "+":
        current_frequency += number
    else:
        current_frequency -= number

print(current_frequency)
