two = 0
three = 0

with open('input.txt') as f:
    for line in f:
        letters = {}
        has_two = False
        has_three = False
        
        for letter in line:
            if not letter in letters:
                letters[letter] = 0
            letters[letter] = letters[letter] + 1
        
        for letter in letters:
            if letters[letter] == 2 and not has_two:
                has_two = True
                two += 1
            if letters[letter] == 3 and not has_three:
                has_three = True
                three += 1

print('two: {}\nthree: {}\ntwo x three = {}'.format(two, three, two * three))
