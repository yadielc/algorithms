'''
splitandjoin.py

Split and Join HackerRank Problem Solution

Instructions:
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

'''
def split_and_join(line):
    # write your code here
    new_line = line.split(" ")
    new_line2 = "-".join(new_line)
    return new_line2
