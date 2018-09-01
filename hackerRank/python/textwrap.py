'''
textwrap.py
Text Wrap HackerRank Problem Solution

Instructions:
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .
'''

def wrap(string, max_width):
    new_string = textwrap.fill(string, max_width)
    return new_string
