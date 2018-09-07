# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
product.py

HackerRank itertools.product() Problem Solution 

'''
import sys,itertools
list1= list(map(int,raw_input().split()))
list2 = list(map(int,raw_input().split()))
print(' '.join(str(e) for e in itertools.product(list1,list2)))
