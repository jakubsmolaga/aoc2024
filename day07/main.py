import sys

lines = sys.stdin.read().split('\n')

def solve1(nums: list[int], target: int, pos: int, value: int) -> bool:
    if pos >= len(nums):
        return value == target
    if solve1(nums, target, pos + 1, value + nums[pos]):
        return True
    if solve1(nums, target, pos + 1, value * nums[pos]):
        return True
    return False


def solve2(nums: list[int], target: int, pos: int, value: int) -> bool:
    if pos >= len(nums):
        return value == target
    if solve2(nums, target, pos + 1, value + nums[pos]):
        return True
    if solve2(nums, target, pos + 1, value * nums[pos]):
        return True
    concatenated = int(str(value) + str(nums[pos]))
    if solve2(nums, target, pos + 1, concatenated):
        return True
    return False

result1 = 0
result2 = 0
for line in lines:
    parts = line.split(': ')
    target = int(parts[0])
    nums = [ int(x) for x in parts[1].split(' ') ]
    if solve1(nums, target, 1, nums[0]):
        result1 += target
    if solve2(nums, target, 1, nums[0]):
        result2 += target

print(result1)
print(result2)
