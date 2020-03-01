# Nathaniel just broke up with Janice. Hence, Janice has become his Ex. In one
# of Nathaniel’s computer science course “Mastering Boolean Expressions”, he
# came across single-variable Boolean expressions, which are made up of:
#
# - The variable x
# - The negation of variable x, X
# - The constant False, 0
# - The constant True, 1
# - The OR operator, | (evaluating to True when at least one of its operands is
# True)
# - The AND operator, & (evaluating to True when both of its operands are True)
# - The XOR operator, ^ (evaluating to True when exactly one of its operands is
# True)
#
# An example of valid expression would be ((x|0)^1), and the expression
# evaluates to True when x == False, and evaluates to False when x == True
# because (False|False)^True) = True and ((True|False)^True) = False.
#
# Sadly, Nathaniel hasn’t gone through completely the grieve of losing his
# utmost loved one. Whenever Nathaniel sees the variables x or X, they remind
# him of his Ex. He is sad, really really sad. After some time, he has had
# enough, he doesn’t want his Ex to affect his emotion anymore. He made up his
# mind to change all the expressions in his textbook so that the final value of
# resulting expressions will not be affected by value of variable x, just like
# his life thereafter will not be affected by his Ex anymore.
#
# For example, using the above expression ((x|0)^1), if Nathaniel modified it
# to ((x|1)|1) (by changing the 5th and 7th characters), then it would evaluate
# to True regardless of value of x. Nevertheless, we can actually achieve that
# by modifying less than 3 characters.
#
# Your task is to calculate the minimum number of character(s), N, needed to
# be changed so that an expression, E, given will evaluate to a same value
# regardless of value x. The expression could be needing no modification as it
# is not affected by x from the beginning.
#
# Note that in Nathaniel’s textbook, there are a few rules for an expression to
# be valid: For example, the following expressions are valid:
#
# - 1
# - (X&0)
# - ((x|1)&x)
#
# While the following expressions are invalid:
#
# - (1)
# - x^0
# - (X&0|x)
#
# You can also safely assume that there are no spaces in the expressions.
#
# Input Format
#
# - Input begins with an integer T, the number of tests.
# - For each test, there is a line containing the expression E.
#
# Constraints
#
# - 1 <= T <= 1000
# - 1 <= |E| <= 300
#
# Output Format
#
# For each expression E in a test, print the lowest modification of
# character(s) needed, N.
#
# Sample Input 0
#
# 4
# 0
# (x^X)
# X
# ((1&(x|1))^X)
#
# Sample Output 0
#
# 0
# 0
# 1
# 1
#
# Explanation 0
#
# - The first expression can be left unchanged (as it always evaluates to
# False).
# - The second expression can be left unchanged (as it always evaluates to
# True).
# - The third expression can, for example, be changed to "1" (and would then
# always evaluate to True).
# - The fourth expression can, for example, be changed to "((1&(x|1))|X)" (and
# would then always evaluate to True).

for _ in range(int(input())):
    s = input()
    print(int(eval(s, dict(x=0, X=1)) != eval(s, dict(x=1, X=0))))
