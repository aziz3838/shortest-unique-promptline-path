#!/usr/bin/env python

# Import
import sys
import os
import subprocess

def main(argv):
    # Read the path value (argument)
    input_path = argv[0]
    
    # Split path
    path_splits = input_path.split('/')
    
    # Delete first split (empty) 
    del path_splits[0]

    # Variable to hold final result
    result = ''

    # Loop though path splits
    for split in xrange(0, len(path_splits) ):
        # Create the intermediate path
        temp_path =  "/" + "/".join(path_splits[0:split])
        
        #Get list of directories in the intermediate path
        dirs = next(os.walk(temp_path))[1]
        
        '''
        # For debugging purposes, use the print statements
        print "Exploring Dir: " + temp_path
        print "That Contains: ", dirs
        print "To Compare with: " + path_splits[split]
        print "----------------------------------------------"
        '''

        # Get shortest unique string for the current split, and append it to the final result
        result = result + "/" + get_shortest(dirs, path_splits[split])
    
    print result
    return result

# Create function to get shortest unique string
def get_shortest(dirs, split_str):
    for char_count in xrange(1, len(split_str)+1):  # len + 1 to include last character
        split_str_sub = split_str[0:char_count]     # The substring we are investigating
        match_count = 0
        for dir in dirs:
            # Find how many directories start with the investigated split_str_sub (sub string)
            if dir.startswith(split_str_sub):
                match_count = match_count + 1
            # Deleting the dir if not match is costly in lists ( O(n) ). ToDo: Find an alternative.
        # If only 1 match is found, then we found the shortest unique string
        if match_count == 1:
            return split_str_sub
    # If more than 1 match kept existing, return the full split_str
    return split_str


if __name__ == "__main__":
    main(sys.argv[1:])
