'''
mutations.py

Mutations: HackerRank Problem Solution

Instructions:
Read a given string, change the character at a given index and then print the modified string.

'''
def mutate_string(string, position, character):
    str = list(string)
    str[position] = character
    string =''.join(str)
    return string
