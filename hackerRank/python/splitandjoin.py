'''
splitandjoin.py

Split and Join HackerRank Problem Solution

'''
def split_and_join(line):
    # write your code here
    new_line = line.split(" ")
    new_line2 = "-".join(new_line)
    return new_line2
