import sys
SLOPE = (3,1) # three to the right, down 1

def create_map(map_file):
    my_map = []
    with open(map_file, 'r+') as open_map:
        for line in open_map:
            my_map.append([char for char in line[:-1]])

    return my_map

def find_point_coordinates(my_map, width, row_index, column_index):
    row_index += SLOPE[1]
    column_index += SLOPE[0]
    
    if column_index >= width:
        column_index = column_index - width
    
    return row_index, column_index


def identify_open_or_tree(my_map, row_index, column_index):
    return my_map[row_index][column_index] == '#'


def main(map_file):
    my_map = create_map(map_file)
    
    # find where need to repeat and where can end
    width = len(my_map[0])
    length = len(my_map)

    # find next point coordinates and count trees
    total_trees = 0
    row_index = 0
    column_index  = 0

    while row_index < length:
        tree = identify_open_or_tree(my_map, row_index, column_index)
        if tree:
            total_trees += 1
        
        row_index, column_index = find_point_coordinates(my_map, width, row_index, column_index)
    
    print(f"Total trees is {total_trees}")



if __name__ == "__main__":
    map_file = sys.argv[-1]
    main(map_file)