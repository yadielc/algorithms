def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0 and year % 100 == 0:
        leap = False;
    elif year % 4 == 0:
        leap = True;
    return leap
