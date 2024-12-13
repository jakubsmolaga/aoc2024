import sys
import numpy as np

def solve(ax: int, ay: int, bx: int, by: int, goalx: int, goaly: int) -> int:
    eq1 = np.array([ax, bx, goalx])
    eq2 = np.array([ay, by, goaly])
    eq1 *= np.lcm(eq1[0], eq2[0]) // eq1[0]
    eq2 *= np.lcm(eq1[0], eq2[0]) // eq2[0]
    eq1 -= eq2
    eq1 *= np.lcm(eq1[1], eq2[1]) // eq1[1]
    eq2 *= np.lcm(eq1[1], eq2[1]) // eq2[1]
    eq2 -= eq1
    if eq1[2] % eq1[1] != 0:
        return 0
    if eq2[2] % eq2[0] != 0:
        return 0
    return (eq1[2] // eq1[1]) + 3 * (eq2[2] // eq2[0])

result1 = 0
result2 = 0
for block in sys.stdin.read().strip().split('\n\n'):
    ax, ay = [int(x[2:]) for x in block.split('\n')[0].split(': ')[1].split(', ')]
    bx, by = [int(x[2:]) for x in block.split('\n')[1].split(': ')[1].split(', ')]
    goalx, goaly = [int(x[2:]) for x in block.split('\n')[2].split(': ')[1].split(', ')]
    result1 += solve(ax, ay, bx, by, goalx, goaly)
    result2 += solve(ax, ay, bx, by, goalx + 10000000000000, goaly + 10000000000000)

print(result1)
print(result2)
