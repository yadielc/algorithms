'''
lists.py

Challenge Instructions:
Consider a list (list = []).

You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

'''
list = []

N = int(raw_input())

for i in range(0, N):
    tokens = raw_input().split()

    if tokens[0] == 'insert':
        list.insert(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'print':
        print L
    elif tokens[0] == 'remove':
        list.remove(int(tokens[1]))
    elif tokens[0] == 'append':
        list.append(int(tokens[1]))
    elif tokens[0] == 'sort':
        list.sort()
    elif tokens[0] == 'pop':
        list.pop()
    elif tokens[0] == 'reverse':
        list.reverse()
