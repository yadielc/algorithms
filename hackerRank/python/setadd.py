'''
setadd.py

Set .add() - HackerRank Problem Solution

'''

N = int(raw_input())

c = set()

for i in range(N):
    c.add(raw_input())

print len(c)
