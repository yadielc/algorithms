'''
collectionscounter.py
https://www.hackerrank.com/challenges/collections-counter/problem

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Concepts reviewed:
1. 

'''
import collections

X = int(raw_input())
sizes = collections.Counter(map(int, raw_input().split()))
N = int(raw_input())

money = 0

for i in range(N):
    (size, price) = map(int, raw_input().split())

    if sizes[size] > 0:
        sizes[size] -= 1
        money += price

print money
