'''
introtosets.py

Introduction To Sets: HackerRank Problem Solution

Instructions:

Calculate the average of the elements, given a set. Use the sum and len functions.

'''

def average(array):
    total = 0
    total = sum(array)
    average = total/len(array)

    return average

# testing code
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
