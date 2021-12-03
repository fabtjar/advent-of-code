with open('input.txt') as f:
    nums = [int(line) for line in f]

prev = nums[0]
increases = 0

for n in nums:
    if n > prev:
        increases += 1
    prev = n

print(increases)
