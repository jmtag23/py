import datetime
import random

def calculateDaysBetweenDates(begins, ends):
    """Calculates the number of days between two given dates"""
    begind = datetime.datetime.strptime(begins, "%Y-%m-%d")
    endd = datetime.datetime.strptime(ends, "%Y-%m-%d")
    deltadays = endd - begind
    return deltadays

def reverse_string(inputStr):
    """Reverses the given string and returns it."""
    return inputStr[::-1]

def parse_expense(expenses_string):
    """Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
    """
    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith("#"):
            continue
        date, value, currency = line.split(" ")
        expenses.append((datetime.datetime.strptime(date, "%Y-%m-%d"),
                            float(value),
                            currency))
    return expenses

def get_random_line(file_path):
    """Reads a file and returns a random line from it."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()
    
def coverter(tempString):
    """Coverts string to float and calculates"""
    return float(tempString)*(9/5)+32

def concatString(s1, s2):
    """Combine two strings and return 1"""
    return s1 + s2

"""still not working"""
    
    