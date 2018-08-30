'''
stringvalidators.py

String Validators HackerRank Problem Solution

'''

if __name__ == '__main__':
    s = raw_input()
    for i in s:
        if i.isalnum():
            print True
        elif i.isalpha():
            print True
        elif i.isdigit():
            print True
        elif i.islower():
            print True
        elif i.isupper():
            print True
        else:
            print False
