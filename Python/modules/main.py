# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
# At the top of your main.py, import a module that prints the Zen of Python.

import sys
import this
from greet import supergreeting
from datetime import datetime
from math import sin
from time import sleep


# Write a function wait that takes one argument -- seconds (int) -- that uses
# a function in the time module to make the computer wait for that number of
# seconds, then returns nothing.

def wait(seconds):
    sleep(seconds)
    return


# Implement a function my_sin that takes one float as an argument and returns
# the sine of that float. Use the math module.

def my_sin(x):
    return sin(x)


# Implement a function iso_now that takes no arguments and returns a string
# containing the current date and time up to the minute in the ISO 8601 format.
# Example: 2000-12-31T17:00. Use the datetime module.

def iso_now():
    return datetime.now().isoformat(timespec='minutes')


# Implement a function platform that takes no arguments and returns a string
# that shows which platform (Linux, Windows, macOS, and so on) we are on.
# Use the sys module.

def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return supergreeting(name)
