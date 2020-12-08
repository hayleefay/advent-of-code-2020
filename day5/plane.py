import sys
import doctest

def get_row_number(row_str):
    '''
    >>> get_row_number('FBFBBFFRLR')
    44.0
    '''
    lower = 0
    upper = 128
    for char in row_str:
        span = (upper - lower)/2
        if char == 'F':
            upper = lower + span
        elif char == 'B':
            lower = lower + span
    
    return lower


def get_seat_number(seat_str):
    '''
    >>> get_seat_number('RLR')
    5.0
    '''
    lower = 0
    upper = 8
    for char in seat_str:
        span = (upper - lower)/2
        if char == 'L':
            upper = lower + span
        elif char == 'R':
            lower = lower + span
    
    return lower


def get_id(row_number, seat_number):
    '''
    >>> get_id(44.0, 5.0)
    357.0
    '''
    return row_number * 8 + seat_number


def get_missing_id(all_ids):
    # find missing ids (although not in rows 0 or 127)
    missings = []
    for row in range(1,126):
        for seat in range(0,8):
            current_id = get_id(row, seat)
            if current_id not in all_ids:
                if current_id + 1 in all_ids and current_id - 1 in all_ids:
                    missings.append(current_id)
    
    return missings


def main(binary_str):
    row_str = binary_str[:7]
    seat_str = binary_str[7:]

    row_number = get_row_number(row_str)
    seat_number = get_seat_number(seat_str)

    seat_id = get_id(row_number, seat_number)

    return seat_id


if __name__ == "__main__":
    doctest.testmod()
    filename = sys.argv[-1]

    all_ids = []
    with open(filename, 'r+') as intput_file:
        for line in intput_file:
            seat_id = main(line[:-1])
            all_ids.append(seat_id)
    
    print("Highest id is", max(all_ids))

    missings = get_missing_id(all_ids)
    print("Not here, but its neighbors are:", missings)
