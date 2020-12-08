import sys
import re


def process_passport(passport):
    passport_dict = {}
    for line in passport:
        pairs = line.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            passport_dict[key] = value
    
    return passport_dict


def check_validity(processed_passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in fields:
        if field not in processed_passport:
            return False
        if field == 'byr':
            if int(processed_passport[field]) < 1920 or int(processed_passport[field]) > 2002:
                return False
        if field == 'iyr':
            if int(processed_passport[field]) < 2010 or int(processed_passport[field]) > 2020:
                return False
        if field == 'eyr':
            if int(processed_passport[field]) < 2020 or int(processed_passport[field]) > 2030:
                return False
        if field == 'hgt':
            if 'cm' not in processed_passport[field] and 'in' not in processed_passport[field]:
                return False
            else:
                height = int(processed_passport[field][:-2].split(' ')[0])
                if 'cm' in processed_passport[field]:
                    if height > 193 or height < 150:
                        return False
                elif 'in' in processed_passport[field]: 
                    if height < 59 or height > 76:
                        return False
        if field == 'hcl':
            if re.search("^#[0-9a-f]{6}", processed_passport[field]) ==  None:
                # print('hcl', processed_passport[field])
                return False
        if field == 'ecl':
            if processed_passport[field] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                # print('ecl', processed_passport[field])
                return False
        if field == 'pid':
            if re.search("^[0-9]{9}$", processed_passport[field]) == None:
                # print('pid', processed_passport[field])
                return False
    
    return True


def main(filename):
    number_valid_passports = 0
    with open(filename, 'r+') as input:
        current_passport = []
        for line in input:
            if line == '\n':
                processed_passport = process_passport(current_passport)
                valid = check_validity(processed_passport)
                if valid:
                    number_valid_passports += 1
                current_passport = []
            else:
                current_passport.append(line[:-1])
    
    if len(current_passport) > 0:
        processed_passport = process_passport(current_passport)
        valid = check_validity(processed_passport)
        if valid:
            number_valid_passports += 1
    
    print(f"Number of valid passports is {number_valid_passports}")


if __name__ == "__main__":
    filename = sys.argv[-1]

    main(filename)

