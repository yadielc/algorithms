'''
setadd.py

Set .add() - HackerRank Problem Solution
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help.
You pick the stamps one by one from a stack of N country stamps.

'''

N = int(raw_input())

c = set()

for i in range(N):
    c.add(raw_input())

print len(c)
