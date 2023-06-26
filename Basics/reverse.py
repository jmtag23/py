import datetime
import random

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