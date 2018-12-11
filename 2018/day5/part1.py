with open('input.txt') as f:
    text = f.read().replace('\n', '')

i = 0
while i + 1 < len(text) - 1:
    a = text[i]
    b = text[i + 1]
    if a.lower() == b.lower() and ((a.islower() and b.isupper()) or (a.isupper() and b.islower())):
        text = text[:i] + text[i + 2:]
        i = max(0, i - 1)
    else:
        i += 1

print(len(text))
