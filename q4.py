# Your little brother is sad, because he can not play Rittileft. So you want to
# help him.
#
# In Rittileft, there is a stright path made of N steps. Each step have two
# numbers, one on the left and one on the right.
#
# You can collect the points by stepping on the number, but you cannot step on
# a number that is divisible by 10.
#
# Your goal is to obtain the maximum sum of the numbers you walk on them.
#
# Input Format
#
# - First line contain single integer
# - Each of the following lines contain two integers R and L
#
# Constraints
#
# - 1 <= N <= 10,000
# - 1 <= R, L <= 1,000
#
# Output Format
#
# - If you brother cannot complete the game, print -1
# - On other cases, print the maximum summ
#
# Sample Input 0
#
# 5
# 8 10
# 3 23
# 10 9
# 56 4
# 4 100
#
# Sample Output 0
#
# 100
#
# Explanation 0
#
# L  | R
# ---+----
# 8  | 10
# 3  | 23
# 10 | 9
# 56 | 4
# 4  | 100
#
# from the top, selecting 8 + 23 + 9 + 56 + 4 which sums up to 100
#
# Sample Input 1
#
# 3
# 9 3
# 200 10
# 88 3
#
# Sample Output 1
#
# -1
#
# Explanation 1
#
# two numbers that are divisible by 10 are blocking the way

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
s = [max((i for i in r if i % 10 != 0), default=None) for r in d]

print(sum(s) if None not in s else -1)
