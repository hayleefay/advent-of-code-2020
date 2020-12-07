'''
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of 
times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at 
least 1 time and at most 3 times.

How many passwords are valid according to their policies?
'''
import sys

def count_valid_passwords(filename):
    with open(filename, 'r+')  as  passwords:
        valid_passwords_count = 0
        for line in passwords:
            rule, password = line.split(': ')
            password = password.split('\n')[0]
            num_rule, letter = rule.split(' ')
            lower, upper = [int(i) for i in num_rule.split('-')]

            num_letters = password.count(letter)
            if num_letters in range(lower, upper+1):
                valid_passwords_count += 1
    
    return valid_passwords_count


if __name__ == "__main__":
    valid_passwords_count = count_valid_passwords(sys.argv[-1])
    print(f"Number of valid passwords: {valid_passwords_count}")