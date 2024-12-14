import sys
import time

board_w = 101
board_h = 103

positions = []
velocities = []
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for line in sys.stdin.read().split('\n'):
    pos, vel = [ [int(x) for x in s[2:].split(',')] for s in line.split(' ') ]
    positions.append(pos)
    velocities.append(vel)
    new_pos = ((pos[0] + vel[0] * 100) % board_w, (pos[1] + vel[1] * 100) % board_h)
    if new_pos[0] == board_w // 2:
        continue
    if new_pos[1] == board_h // 2:
        continue
    if new_pos[0] < board_w // 2 and new_pos[1] < board_h // 2:
        q1 += 1
    elif new_pos[0] > board_w // 2 and new_pos[1] < board_h // 2:
        q2 += 1
    elif new_pos[0] > board_w // 2 and new_pos[1] > board_h // 2:
        q3 += 1
    elif new_pos[0] < board_w // 2 and new_pos[1] > board_h // 2:
        q4 += 1

print(q1*q2*q3*q4)

for seconds in range(20000):
    board = [[' '] * board_w for _ in range(board_h)]
    for i in range(len(positions)):
        x, y = positions[i]
        board[y][x] = '█'
        dx, dy = velocities[i]
        positions[i] = ((x + dx) % board_w, (y + dy) % board_h)
    has_straight_line = False
    for line in board:
        if '██████████' in ''.join(line):
            has_straight_line = True
            break
    if has_straight_line:
        print(seconds, '---------------------------------------------------------------------------------')
        print()
        print('\n'.join([''.join(line) for line in board]))
        print()
        break
