def sliding_window(nums):
    i = 0
    while i + 3 <= len(nums):
        yield sum(nums[i:i+3])
        i += 1


with open('input.txt') as f:
    nums = [int(line) for line in f]

prev = None
increases = 0

for n in sliding_window(nums):
    if prev is None:
        prev = n

    if n > prev:
        increases += 1
    prev = n

print(increases)
