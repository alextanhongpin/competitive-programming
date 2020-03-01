# Let's play Python.
#
# You are given a matrix n x m, which represent a map of a Python game. The map
# contains # which is a wall you cannot pass, . which is an empty space, @
# which is the apple (goal), or a digit(1-9) which represent Python's body.
# Python's body begins with 1 as its head and extends to l body segments which
# are adjacent to each other, meaning that segment[i] and segment[i+1] share a
# common side.
#
# During the game, Python moves through the map to reach the apple, during one
# move Python can move it's head to an adjacent field of the map and the rest
# of the body will follow. segment[i] would move to the place segment[i - 1]
# was at.
#
# All segments move at the same time. meaning that Python can move like
# follows:
#
# 1 2
# 4 3
#
# to
#
# 2 3
# 1 4
#
# If Python moves into a wall or into one of its body segments, Python would
# die and it would be Game Over.
#
# Your goal is to determine the minimum number of moves Python can use to reach
# the apple without dying.
#
# Input Format
#
# - The first line contains n and m, which are the number of rows and columns
# in the map.
# - The next n lines, contain m characters #, ., @, 1-9.
#
# Constraints
#
# - 1 <= n, m <= 15
# - 3 <= |Python| <= 9 (the length of Python)
#
# Output Format
#
# Print a single integer which is the minimum number of moves needed, or -1 if
# Python cannot reach the apple.
#
# Sample Input 0
#
# 4 5
# ##...
# ..1#@
# 432#.
# ...#.
#
# Sample Output 0
#
# 4
#
# Sample Input 1
#
# 4 4
# #78#
# .612
# .543
# ..@.
#
# Sample Output 1
#
# 6

from collections import OrderedDict, deque


h, w = list(map(int, input().split()))
m = {(x, y): c for y in range(h) for x, c in enumerate(input())}
# m = OrderedDict(sorted(m.items(), key=lambda k: k[1]))  # debug map
python = tuple(sorted((p for p, c in m.items() if '1' <= c <= '9'), key=m.get))
for p in python:  # clear python from map
    m[p] = '.'

# breadth first search
q = deque([(0, python)])  # queue - distance, python
v = set()                 # visited python path
s = None                  # best score
while q:
    e, p = q.popleft()

    if s is not None and e >= s:  # if more efficient solution calculated
        continue
    if m[p[0]] == '@':
        s = e
        continue

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n = (p[0][0] + dx, p[0][1] + dy)
        if 0 <= n[0] < w and 0 <= n[1] < h and m[n] != '#' and \
           n not in p[:-1] and (n, *p[:-1]) not in v:
            q.append((e + 1, (n, *p[:-1])))

    v.add(p)

    # print(e)
    # for y in range(h):
    #     for x in range(w):
    #         print(str(1 + p.index((x, y))) if (x, y) in p else m[(x, y)],
    #               end='')
    #     print()
    # print()

print(s or -1)
