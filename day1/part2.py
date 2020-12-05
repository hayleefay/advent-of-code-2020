'''
They offer you a second one if you can find three numbers in your expense 
report that meet the same criteria.

In your expense report, what is the product of the three entries that sum to 2020?
'''
import sys
import doctest
import pandas as pd

def find_nums_that_sum(expenses, num=2020):
    '''
    This function finds three numbers in the sequence that sum to num
    and returns them.

    >>> find_nums_that_sum([2000, 10, 10, 40])
    (2000, 10, 10)
    '''
    expenses_set = set(expenses)
    for i, val1 in enumerate(expenses):
        for j, val2 in enumerate(expenses):
            val3 = num - val1 - val2
            if val3 in expenses_set:
                return val1, val2, val3


if __name__ == "__main__":
    doctest.testmod()

    df = pd.read_csv(sys.argv[-1])
    e1, e2, e3 = find_nums_that_sum(df['amount'].values)

    print(f'Answer: {e1 * e2 * e3}')
