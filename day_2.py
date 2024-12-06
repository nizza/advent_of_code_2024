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
        
def check_report(original_report):
    
    # changing the order of the list (last to first)
    # if the first 2 elements are not in increasing order
    if original_report[0] > original_report[1]:
        report =  original_report[::-1]
    else:
        report = original_report

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


def check_report_2_increasing(report):
    """
    Checks if report is safe in either increasing order.
    """
    
    def check_report_right(report, i):
        """
        return a new list, where the element at position i is a boolean
        inidicating  whether the subreport starting at position i+1 is 
        safe (increasing)
        """
        
        # base case, empty list or 1 element
        if i == len(report) - 1:
            return [True]
        elif i == len(report) - 2:
            return [True] + check_report_right(report, i+1)
        # checking recursively the rest of the report
        else:
            diff = report[i+2] - report[i+1]
            remainder_check = check_report_right(report, i+1)
            current_check = remainder_check[0]  and (diff >= 1) and (diff <= 3)
            full_check = [current_check] + remainder_check
            return full_check
    
    def check_report_left(report, i):
        """
        return a new list, where the element at position i is a boolean
        inidicating  whether the subreport ending at position i-1 is 
        safe (increasing)
        """
        
        # base case, empty list or 1 element
        if i == 0:
            return [True]
        elif i == 1:
            return check_report_left(report, i-1) +[True]
        # checking recursively the rest of the report
        else:
            diff = report[i-1] - report[i-2]
            remainder_check = check_report_left(report, i-1)
            current_check = (diff >= 1) and (diff <= 3) and remainder_check[-1]
            full_check = remainder_check +  [current_check] 
            return full_check
    
        
    right_check = check_report_right(report, 0)
    left_check = check_report_left(report, len(report)-1)
    
    # a report is totally is safe if all the elements right of the 1st one are safe
    # and the difference between 1st and 2nd 1 <= diff <= 3
    diff = report[1] - report[0]
    if right_check[0] and diff >= 1 and diff <= 3:
        return True
    
    # a report is partially safe if totally safe after removing the first
    # or last element
    if right_check[0] or left_check[-1]:
        return True
    
    # a report is partially safe is it exists at least a position i, 0<i<N-1
    # for which both the left report and right report are safe
    # and the distance between left and right is   1 <= diff <= 3
    is_safe = False
    for i in range(1, len(report)-1):
        diff = report[i+1] - report[i-1]
        if right_check[i] and left_check[i] and diff >= 1 and diff <= 3:
            is_safe = True
            break
    
    return is_safe
    
def check_report_2(report):
    """
    Checks if report is safe in either increasing or decreasing order
    """
    return (check_report_2_increasing(report) or
            check_report_2_increasing(report[::-1]))
    
    

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
    
    # Computing result for part 2
    print("Part 2:")
    result = sum([check_report_2(report) for report in reports])
    print(result)
    print()
    
    

