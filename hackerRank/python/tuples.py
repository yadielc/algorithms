'''
tuples.py

Tuples Challenge on HackeRrank python
https://www.hackerrank.com/challenges/python-tuples

'''
if __name__ == '__main__':
    n = int(raw_input())
    t = tuple(map(int, raw_input().split()))

print hash(t)
