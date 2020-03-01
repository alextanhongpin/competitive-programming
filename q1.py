# Ahmad is a system administrator. He handles Linux server. He uses a variant
# of ps utility to monitor which process it taking up most memory.
#
# Ahmad needs to sort the ps output by the ppid which is the parents process id
# and then by its mem which is memory. He is more interested about process that
# use more memory, so mem should be sorted in decreasing order.
#
# Given a sample ps output as input, generate another ps output in increasing
# ppid, then decreasing mem. If two process share the same ppid and mem, keep
# the original relative ordering of the two process.
#
# Input Format
#
# - The input first start with a header row, which have three constant word
# "pid", "ppid" and "mem" separated by a space.
#
# - The several lines each consist of three integer a, b, c, where is the pid
# or process id, b is the ppid or parent process id, and c is the mem or
# memory.
#
# Constraints
#
# 0 <= a, b, c <= 10⁵
#
# Output Format
#
# Output the sorted ps output in the same format as the input.
#
# Sample Input 0
#
# pid ppid mem
# 1 0 12
# 2 1 22
# 4 1 92
# 100 4 98
# 101 4 92
#
# Sample Output 0
#
# pid ppid rss
# 1 0 12
# 4 1 92
# 2 1 22
# 100 4 98
# 101 4 92
#
# Sample Input 1
#
# pid ppid mem
# 1 0 12
# 2 1 22
# 4 1 92
# 103 1 92
# 102 4 98
# 101 4 94
# 100 4 98
#
# Sample Output 1
#
# pid ppid rss
# 1 0 12
# 4 1 92
# 103 1 92
# 2 1 22
# 102 4 98
# 100 4 98
# 101 4 94
#
# Explanation 1
#
# Notice that process 102 appears before 100 in the input, therefore in the
# output, 102 appears before 100, no reordering between these two process as
# they have the same parent and memory usage.

import sys

_ = input()
d = [list(map(int, r.split())) for r in sys.stdin]

print("pid ppid rss")
for r in sorted(d, key=lambda k: (k[1], -k[2])):
    print(' '.join(map(str, r)))
