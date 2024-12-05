import sys
import functools

ordering_section, updates_section = sys.stdin.read().split('\n\n')

ordering_rules = set(ordering_section.strip().split('\n'))

def cmp(a: int, b: int) -> int:
    if f"{a}|{b}" in ordering_rules:
        return -1
    if f"{b}|{a}" in ordering_rules:
        return 1
    return 0

key = functools.cmp_to_key(cmp)

result1 = 0
result2 = 0
for update in updates_section.split('\n'):
    nums = [int(x) for x in update.split(',')]
    sorted_nums = sorted(nums[:], key=key)
    if sorted_nums == nums:
        result1 += nums[len(nums) // 2]
    else:
        result2 += sorted_nums[len(sorted_nums) // 2]

print(result1)
print(result2)
