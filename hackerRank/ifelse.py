#!/bin/python3

'''
Hacker Rank Challenge: Python If-Else

Instructions:

If N is odd print "Weird"

'''

N = int(input())


if N % 2 != 0:
    print ("Weird")
elif N % 2 == 0 and 2 <= N <=5:
    print("Not Weird")
elif N % 2 == 0 and 6 <= N <= 20:
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
