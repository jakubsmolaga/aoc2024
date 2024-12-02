import sys

lines = sys.stdin.read().split('\n')

reports = [ [ int(x) for x in line.split(' ') ] for line in lines ]

def is_safe_report(report: list[int]) -> bool:
    x = sorted(report)
    r = list(reversed(report))
    if not (report == x or r == x):
        return False
    safe = True
    for i in range(len(report) - 1):
        d = abs(report[i] - report[i+1])
        if d < 1 or d > 3:
            safe = False
    return safe

result1 = 0
for report in reports:
    x = sorted(report)
    r = list(reversed(report))
    if not (report == x or r == x):
        continue
    safe = True
    for i in range(len(report) - 1):
        d = abs(report[i] - report[i+1])
        if d < 1 or d > 3:
            safe = False
    if safe:
        result1 += 1

print(result1)

result2 = 0
for report in reports:
    is_safe = False
    for i in range(len(report)):
        arr = report[:i] + report[i+1:]
        if is_safe_report(arr):
            is_safe = True
            continue
    if is_safe:
        result2 += 1
        
    # increasing_pairs = 0
    # decreasing_pairs = 0
    # wrong_distances = 0
    # for i in range(len(report) - 1):
    #     if report[i] > report[i + 1]:
    #         decreasing_pairs += 1
    #     elif report[i] < report[i + 1]:
    #         increasing_pairs += 1
    #     d = abs(report[i] - report[i+1])
    #     if d < 1 or d > 3:
    #         wrong_distances += 1
    # total_mistakes = 0
    # if increasing_pairs > decreasing_pairs:
    #     total_mistakes += decreasing_pairs
    # else:
    #     total_mistakes += increasing_pairs
    # total_mistakes += wrong_distances
    # print('report: ', report)
    # print('total_mistakes: ', total_mistakes)
    # print()
    # if total_mistakes > 1:
    #     continue
    #
    # if total_mistakes <= 1:
    #     result2 += 1

print(result2)
