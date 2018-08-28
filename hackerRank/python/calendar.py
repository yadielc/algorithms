'''
calendar.py
Calendar Module: HackerRank Problem Solution

Instructions:
You are given a date. Your task is to find what the day is on that date.

'''

import calendar

date = raw_input().strip().split()

days = list(calendar.day_name)
print days[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))].upper()
