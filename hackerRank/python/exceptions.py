# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Author Yadiel F. Cabrera
exceptions.py

Exceptions Hacker Rank Problem Solution
https://www.hackerrank.com/challenges/exceptions/problem

Instructions:
You are given two values a and b .
Perform integer division and print a/b.

Concepts reviewed:
exceptions - https://docs.python.org/3/tutorial/errors.html
'''

l = int(raw_input()) # gather input from the user

# check the values, perform the operation and print the exceptions
for i in range(0, l):
    try:
        a, b = map(int, raw_input().split())
        print a/b
    except ZeroDivisionError as e:
        print "Error Code:", e
    except ValueError as e:
        print "Error Code:", e
