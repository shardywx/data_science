# Problem taken from link below
# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Given a year, determine whether it is a leap year (return True if so, False if not). 

def is_leap(year: int):
    """
    Input an integer and determine whether the year is a leap year or not
    """
    leap = False
    
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap

year = int(input())
