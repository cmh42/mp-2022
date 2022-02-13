#!/usr/bin/env python

import sys

def peek_at_file(file_name,num_lines=15,line_numbering=False): 
    """
    Function that takes 3 inputs: file_name, num_lines (optional, default 15), 
    line_numbering (optional, default False). Prints our first num_lines many 
    lines of the file called file_name. Line number printed out first for each line 
    if line_numbering set to True. Function returns None. 
    """
    line_number = 1
    with open(file_name,'r') as file: 
        for line in file: 
            if line_numbering: 
                print("{:<3d}".format(line_number) +  line.rstrip('\n'))
            else: 
                print(line.rstrip('\n'))
            line_number += 1
            if line_number > num_lines: 
                break
    return None 

def main():
    num_args = len(sys.argv)
    if not (num_args > 1 and num_args < 5):
        print("Nothing done.  You need to enter:  ")
        print("$ ./peek_at_file.py file_name num_lines line_numbering_switch")
        print("or")
        print("$ ./peek_at_file.py file_name num_lines")
        print("or")
        print("$ ./peek_at_file.py file_name num_lines")
        print("or")
        print("$ python peek_at_file.py file_name num_lines line_numbering_switch")
        print("etc")
        return None

    file_name = sys.argv[1]
    switch_val = False
    if num_args == 4:
        switch = sys.argv[3]
        if switch[0] in "tT":
            switch_val = True
        peek_at_file(file_name,int(sys.argv[2]),switch_val)
    elif num_args == 3:
        peek_at_file(file_name,int(sys.argv[2]))
    else:
        peek_at_file(file_name)


if __name__ == '__main__': 
    main()


