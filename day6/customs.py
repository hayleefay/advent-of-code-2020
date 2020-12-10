import doctest
import sys

def get_number_of_questions(group):
    '''
    >>> get_number_of_questions(['a','b','x','c','b'])
    4
    '''
    group_set = set(group)
    num_questions = len(group_set)

    return num_questions


if __name__ == "__main__":
    doctest.testmod()
    filename = sys.argv[-1]

    # part 1
    all_groups = []
    with open(filename, 'r+') as inputs:
        group = []
        for line in inputs:
            if line == '\n':
                all_groups.append(get_number_of_questions(group))
                group = []
            else:
                group += [char for char in line[:-1]]
    
    if len(group) > 0:
        all_groups.append(get_number_of_questions(group))
    
    print("Total questions anyone answered:", sum(all_groups))

    # part 2
    intersection_groups = []
    first = True
    with open(filename, 'r+') as inputs:
        intersection_group = set()
        for line in inputs:
            if line == '\n':
                intersection_groups.append(len(intersection_group))
                intersection_group = set()
                first = True
            elif first:
                new_set = set([char for char in line[:-1]])
                intersection_group = intersection_group | new_set
                first = False
            else:
                intersection_group = intersection_group.intersection(set([char for char in line[:-1]]))
    
    if len(intersection_group) > 0:
        intersection_groups.append(len(intersection_group))
            
    print("Total questions everyone answeered:", sum(intersection_groups))
