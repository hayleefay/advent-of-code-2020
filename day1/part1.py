'''
Before you leave, the Elves in accounting just need you to fix your expense report 
(your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply 
those two numbers together.

Find the two entries that sum to 2020; what do you get if you multiply them together?
'''
import doctest
import pandas as pd
import sys

def find_nums_that_sum(expenses, num=2020):
    '''
    This function finds two numbers that sum to a value
    from a sequence of numbers and returns them.

    >>> find_nums_that_sum([2020, 0, 100])
    (2020, 0)
    '''
    expenses_set = set(expenses)
    for e1 in expenses:
        e2 = num - e1
        if e2 in expenses_set:
            return e1, e2


if __name__ == "__main__":
    doctest.testmod()

    df = pd.read_csv(sys.argv[-1])
    e1, e2 = find_nums_that_sum(df['amount'].values)

    print(f'Answer: {e1 * e2}')
