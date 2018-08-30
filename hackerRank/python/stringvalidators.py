'''
stringvalidators.py


'''

if __name__ == '__main__':
    s = raw_input()
    for i in s:
        if i.isalnum():
            print True
        if i.isalpha():
            print True
        if i.isdigit():
            print True
        if i.islower():
            print True
        if i.isupper():
            print True
        else:
            print False
