import string

with open('input.txt') as f:
    full_text = f.read().replace('\n', '')

shortest = len(full_text)
for letter in string.ascii_lowercase:
    text = full_text
    text = text.replace(letter, '')
    text = text.replace(letter.upper(), '')
    
    i = 0
    while i + 1 < len(text) - 1:
        a = text[i]
        b = text[i + 1]
        if a.lower() == b.lower() and (
                (a.islower() and b.isupper()) or (a.isupper() and b.islower())):
            text = text[:i] + text[i + 2:]
            i = max(0, i - 1)
        else:
            i += 1
    if len(text) <= shortest:
        shortest = len(text)

print(shortest)
