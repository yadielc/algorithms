'''
designerdoormat.py
Designer Door Mat Hacker Rank Solution

Concepts reviewed:
x-range - Creates a list of values as you need them, using yielding. Uses generators
for this.

'''
#get mat specs
N, M = map(int, raw_input().split())

#
for i in xrange(1, N, 2):
    print str('.|.' * i).center(M, '-')
print 'WELCOME'.center(M, '-')
for i in xrange(N-2, -1, -2):
    print str('.|.' * i).center(M, '-')
