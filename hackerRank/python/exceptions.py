# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
 exceptions.py
 Exceptions Hacker Rank problem solution

'''

l = int(raw_input())

for i in range(0, l):
    try:
        a, b = map(int, raw_input().split())
        print a/b
    except ZeroDivisionError as e:
        print "Error Code:", e
    except ValueError as e:
        print "Error Code:", e
