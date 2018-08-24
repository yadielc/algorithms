'''
mutations.py

Mutations: HackerRank Problem Solution 
'''
def mutate_string(string, position, character):
    str = list(string)
    str[position] = character
    string =''.join(str)
    return string
