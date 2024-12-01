import sys

lines = sys.stdin.read().strip().split('\n')
pairs = [line.split('  ') for line in lines]
l_nums: list[int] = []
r_nums: list[int] = []
for pair in pairs:
    l_nums.append(int(pair[0]))
    r_nums.append(int(pair[1]))
l_nums.sort()
r_nums.sort()

result1 = 0
for i in range(len(l_nums)):
    result1 += abs(l_nums[i] - r_nums[i])
print(result1)

result2 = 0
counts = dict[int, int]()
for num in r_nums:
    counts[num] = 0
for num in r_nums:
    counts[num] += 1
for num in l_nums:
    if num in counts:
        result2 += num * counts[num]
print(result2)
