import sys
import re

inp = sys.stdin.read().strip()

matches: list[str] = re.findall("mul\\([0-9]+,[0-9]+\\)", inp)

result1 = 0
for m in matches:
    m = m.replace('mul(', '')
    m = m.replace(')', '')
    a, b = [ int(x) for x in m.split(',') ]
    result1 += a * b

print(result1)

result2 = 0
matches = re.findall("(mul\\([0-9]+,[0-9]+\\))|(don't)|(do)", inp)
enabled = True
for m, disable, enable in matches:
    if disable != '':
        enabled = False
        continue
    if enable != '':
        enabled = True
        continue
    if enabled == False:
        continue
    m = m.replace('mul(', '')
    m = m.replace(')', '')
    a, b = [ int(x) for x in m.split(',') ]
    result2 += a * b

print(result2)
