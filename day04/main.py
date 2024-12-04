import sys
import re

def trans(M):
    return [''.join([M[j][i] for j in range(len(M))]) for i in range(len(M[0]))]

lines = sys.stdin.read().split('\n')

result1 = 0

# horizontal
for line in lines:
    for _ in re.findall("XMAS", line):
        result1 += 1
    for _ in re.findall("SAMX", line):
        result1 += 1

# vertical
for column in trans(lines):
    for _ in re.findall("XMAS", column):
        result1 += 1
    for _ in re.findall("SAMX", column):
        result1 += 1

# diagonal
for row in range(0, len(lines) - len("XMAS") + 1):
    for col in range(0, len(lines) - len("XMAS") + 1):
        a = lines[row + 0][col + 0]
        b = lines[row + 1][col + 1]
        c = lines[row + 2][col + 2]
        d = lines[row + 3][col + 3]
        if a == 'X' and b == 'M' and c == 'A' and d == 'S':
            result1 += 1
        if a == 'S' and b == 'A' and c == 'M' and d == 'X':
            result1 += 1
for row in range(len("XMAS") - 1, len(lines)):
    for col in range(0, len(lines[0]) - len("XMAS") + 1):
        a = lines[row - 0][col + 0]
        b = lines[row - 1][col + 1]
        c = lines[row - 2][col + 2]
        d = lines[row - 3][col + 3]
        if a == 'X' and b == 'M' and c == 'A' and d == 'S':
            result1 += 1
        if a == 'S' and b == 'A' and c == 'M' and d == 'X':
            result1 += 1

print(result1)

result2 = 0
for row in range(0, len(lines) - len("MAS") + 1):
    for col in range(0, len(lines[0]) - len("MAS") + 1):
        a1 = lines[row + 0][col + 0]
        b1 = lines[row + 1][col + 1]
        c1 = lines[row + 2][col + 2]
        a2 = lines[row + 0][col + len("MAS") - 1]
        b2 = lines[row + 1][col + len("MAS") - 2]
        c2 = lines[row + 2][col + len("MAS") - 3]
        txt1 = a1 + b1 + c1
        txt2 = a2 + b2 + c2
        forward1 = txt1 == 'MAS'
        forward2 = txt2 == 'MAS'
        backward1 = txt1 == 'SAM'
        backward2 = txt2 == 'SAM'
        valid = (forward1 or backward1) and (forward2 or backward2)
        if valid:
            matched_lines = lines[row:row+3]
            printable = '\n'.join([line[col:col+3] for line in matched_lines])
            result2 += 1

print(result2)
