'''
textwrap.py
Text Wrap HackerRank Problem Solution

'''

def wrap(string, max_width):
    new_string = textwrap.fill(string, max_width)
    return new_string
