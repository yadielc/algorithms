'''
listcomprehensions.py
https://www.hackerrank.com/challenges/list-comprehensions/problem

List Comprehensions HackerRank Problem Solution

You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n
and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y)

Concepts reviewed:
1. List comprehensions
'''
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    #List comprehension
    list = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z !=n]

    #Output the result
    print(list)
