import os
import argparse
import re


        
def get_operands(line):
    
    # initializing results
    res= []
    
    # extracting matches from line
    instructions = re.findall("(mul\(([0-9]{1,3}),([0-9]{1,3})\))", line)
    
    # extracting operands from each instruction
    for inst in instructions:
        #res.append((inst[1], inst[2]))
        res.append((int(inst[1]), int(inst[2])))
        
    return res




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store', dest='input_file',
                    help='Path to the input file')
    args = parser.parse_args()

    # Reading the input file
    with open(args.input_file, 'r') as input_file:
        lines = input_file.readlines()
        
    # concatenating the lines in one single line
    line = ''.join(lines)
    
    # Computing result for part 1
    print("Part 1:")
    # extracting the operands from the line
    opreands_list = get_operands(line)
    # multiplying the operands, and summing
    result = sum([a*b for (a,b) in opreands_list])
    print(result)
    print()
     
    

