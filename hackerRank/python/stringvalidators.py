'''
https://www.hackerrank.com/challenges/string-validators/problem
stringvalidators.py

String Validators HackerRank Problem Solution

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters,
 alphabetical characters, digits, lowercase and uppercase characters.

Review of Concepts:

- any function: https://docs.python.org/3/library/functions.html#anys
  


'''

if __name__ == '__main__':
    s = raw_input()
    print(any(c.isalnum() for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))
