'''
print.py
HackerRank Problem Solution: Print Function

This program prints from 1 to N all in one line as indicated in exercise instructions. 

'''

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print (i, end='')
