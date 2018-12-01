#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:20:26 2018

@author: alemeneses
"""

#%%
# Modify your ecommerce example so, instead of returning None when two services
#  of the same type happen on checkout, raises an exception



class SerceDuplicatedException (Exception):
    if shopping_cart == []: 
        print("go back shopping")
        return None 
    
#%%
        
# Create a function that reads through a file and prints all the lines in 
# uppercase.

# be sure to control exceptions that may occur here, such as the file not 
# existing
        
def print_file_uppercase(filename):
    
    try:
        file = open(filename)
        
        file = open(filename)
        
        for line in file: 
            print (line.upper().strip())
    
    except Exception:
        print("file does not exisit my brother")
            
print_file_uppercase("data.txt")

def parse_csv(filename, separator=","): 
    
    try:
        file = open(filename)
        csv= []
        
        for line in file: 
            line.strip().split(separator)
        return csv
    
    except Exception: 
        print("something went wrong")

csv = parse_csv("data.csv")


# The function must receive two names (origin and destination, for example),
#  and copy the contents of origin into destination.

# You'll need to investigate how to write files for this exercise

def copy_file(origin, destination):

    try: 
        origin_file = open(origin)
        destination_file = open(destination, "w")
    
        # if len(origin_file.read) ==0:
        for line in origin_file: 
            destination_file.write(line)
            
        destination_file.close()
    
    except Exception :
        print("something went wrong" )
    








