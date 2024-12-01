import os
import argparse
import re

def parse_lines(lines):
    
    # initializing results
    list_A, list_B = [], []

    for line in lines:
        
        # splitting the line in two
        substrings = line.split()
        str_a = substrings[0]
        str_b = substrings[1]
        
        # casting to int
        num_a = int(str_a)
        num_b = int(str_b)
        
        # storing the results
        list_A.append(num_a)
        list_B.append(num_b)
        
    return list_A, list_B
        
def compute_diffs(list_A, list_B):
    
    # initializing results
    res= []
    
    # sorting the lists
    list_A = sorted(list_A)
    list_B = sorted(list_B)
    
    # creating list of diffs
    for a,b in zip(list_A, list_B):
        res.append(abs(a-b))
        
    return res


    




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store', dest='input_file',
                    help='Path to the input file')
    args = parser.parse_args()

    # Reading the input file
    with open(args.input_file, 'r') as input_file:
        lines = input_file.readlines()
    
    # Parsing the lines into 2 list of integers
    list_A, list_B = parse_lines(lines)
    
    # Computing result for part 1
    print("Part 1:")
    result = sum(compute_diffs(list_A, list_B))
    print(result)
    print()
    

