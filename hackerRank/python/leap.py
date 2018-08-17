'''
leap.py

You are given the year, and you have to write a function to check if the year is leap or not.
'''
def is_leap(year):
    leap = False
    # if year is evenly divisible by 400, then it's a leap year 
    if(year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100 != 0):
        leap = True
    return leap
