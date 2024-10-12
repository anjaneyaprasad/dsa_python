# test on print
import string

print('''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
''')

# python version

import sys

print("Python version")
print(sys.version)
print(sys.version_info)

# Display date & time:

import datetime

print(datetime.datetime.now())

now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Area of circle:
import math


def area_of_circle(r: float):
    return math.pi * math.pow(r, 2)


print(area_of_circle(1.1))


# accept sequence of numbers and convert to list & tuples

# values = input("Input comma separated numbers")
#
# in_list = values.split(",")
# print(in_list)
#
# in_tuple = tuple(in_list)
# print(in_tuple)

# prints extension of the file

def file_extension(f: string):
    return f.split('.')[-1]


print(file_extension("anjaneya.java"))
print(file_extension("my.doc.py"))

# show first and last colours from the list
colour_list = ["Red", "Green", "White", "Black"]
print(colour_list[0] + " " + colour_list[-1])
print("%s, %s" % (colour_list[0], colour_list[-1]))

# display exam start date

exam_st_date = (11, 12, 2014)
print("%i / %i / %i" % exam_st_date)


# compute n+nn+nnn

def compute(n):
    return n + math.pow(n, 2) + math.pow(n, 3)


print(compute(5))

# help of functions

# print(help(abs))
print(abs.__doc__)

# print calendar

import calendar


def print_calendar(year: int, month: int):
    print(calendar.month(year, month))


print_calendar(2024, 2)

# print here document

print('''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')

# difference in days

from datetime import date


def diff_dates(date1: tuple, date2: tuple):
    return (date(date2[0], date2[1], date2[2]) - date(date1[0], date1[1], date1[2])).days


print(diff_dates((2014, 7, 2), (2014, 7, 11)))


# volume of sphere

def sphere_volumne(radius: float):
    return math.pi * math.pow(radius, 3) * 4 / 3


print(sphere_volumne(6))


# difference between 'number' and 17

def difference_17_number(number: int):
    if number > 17:
        return 2 * (number - 17)
    else:
        return 17 - number


print(difference_17_number(15))
print(difference_17_number(25))

# is within range

def is_within_range(number: int):
    if number <= 100:
        return "between 0 and 100"
    elif number > 100 and number <= 1000:
        return "between 100 and 1000"
    else:
        return "more than 1000"

print(is_within_range(75))
print(is_within_range(705))

# sum of numbers

def sum_of_numbers(n1, n2, n3):
    sum = n1 + n2 + n3
    if n1 == n2 and n2 == n3:
        sum *= 3
    return sum

print(sum_of_numbers(3, 3, 3))
print(sum_of_numbers(1, 2, 3))

