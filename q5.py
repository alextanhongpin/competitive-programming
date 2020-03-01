# One of the most and ancient tactics in war is encirclement. It works by
# surrounding the position to isolate enemy forces. The most common reasons is
# to actually prevent outside reinforcements and supplies.
#
# With having the enemy forces encircled, attacker can focus on attacking
# multiple enemy points in the inner circle. When this happens, defender (those
# inside the circle) either must fight to the death in order for them to break
# the encirclement, or surrender.
#
# [Encirclement image - outer points of polygon are selected only]
#
# You, as Admiral General Aladeen most trusted programmer, has been instructed
# to create a program, which can calculate which enemy units to attack with the
# intention of creating encirclement for inner enemy units. One strict
# condition that he asked is to never let enemy units to be outside of the
# encirclement, or else disaster will happen. Beware, you don’t want to
# disappoint Aladeen, right?
#
# Input Format
#
# - First line of input is an integer N, where N is the number of enemy units.
# - For the next N lines, there are two integers X and Y, where these denote
# point coordinates of enemy units.
#
# Constraints
#
# - 3 <= N <= 100
# - 0 <= X, Y <= 1,000
#
# Output Format
#
# Output all point coordinates of enemy units to attack based on Admiral
# General Aladeen instruction above. Output the points sorted by X then by Y.
#
# Sample Input 0
#
# 6
# 2 2
# 4 4
# 3 4
# 4 3
# 3 6
# 6 3
#
# Sample Output 0
#
# 2 2
# 3 6
# 6 3

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
previous = last = points.index(min(points))
hull = []

# convex hull
while True:
    hull.append(points[previous])
    current = (previous + 1) % n

    for n, p in enumerate(points):
        # right of by orientation (convex)
        if (p[1] - points[previous][1]) * (points[current][0] - p[0]) - \
           (p[0] - points[previous][0]) * (points[current][1] - p[1]) < 0:
            current = n

    previous = current
    if previous == last:
        break

for point in sorted(hull):
    print(point[0], point[1])
