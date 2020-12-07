'''
Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, 
and so on. (Be careful; Toboggan Corporate Policies have no concept 
of "index zero"!) Exactly one of these positions must contain the 
given letter. Other occurrences of the letter are irrelevant for 
the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''

import sys

def count_valid_passwords(filename):
    with open(filename, 'r+')  as  passwords:
        valid_passwords_count = 0
        for line in passwords:
            rule, password = line.split(': ')
            password = password.split('\n')[0]
            num_rule, letter = rule.split(' ')
            first_pos, second_pos = [int(i) for i in num_rule.split('-')]

            if password[first_pos-1] == letter and password[second_pos-1] != letter:
                valid_passwords_count += 1
            elif password[first_pos-1] != letter and password[second_pos-1] == letter:
                valid_passwords_count += 1
    
    return valid_passwords_count


if __name__ == "__main__":
    valid_passwords_count = count_valid_passwords(sys.argv[-1])
    print(f"Number of valid passwords: {valid_passwords_count}")