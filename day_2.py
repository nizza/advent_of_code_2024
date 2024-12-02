import os
import argparse
import re

def parse_lines(lines):
    
    # initializing result
    reports =  []

    for line in lines:
        
        # splitting the line
        report = line.split()
        
        # casting to int
        report = [int(value) for value in report]
        
        # storing the results
        reports.append(report)
        
    return reports
        
def check_report(report):
    
    # changing the order of the list (last to first)
    # if the first 2 elements are not in increasing order
    if report[0] > report[1]:
        report =  report[::-1]

    # checking if conditions are respected for all elements
    valid = 0
    for i in range(1, len(report)):
        if (report[i] - report[i-1]) < 1:
            break
        if (report[i] - report[i-1]) > 3:
            break
        valid += 1

    # the report is safe if all checks were successfull 
    if valid == len(report) -1:
        return True
    else:
        return False
    




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store', dest='input_file',
                    help='Path to the input file')
    args = parser.parse_args()

    # Reading the input file
    with open(args.input_file, 'r') as input_file:
        lines = input_file.readlines()
    
    # Parsing the reports
    reports = parse_lines(lines)
    
    # Computing result for part 1
    print("Part 1:")
    result = sum([check_report(report) for report in reports])
    print(result)
    print()
    


