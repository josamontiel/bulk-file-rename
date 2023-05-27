#!/usr/bin/env python3

# python script to test the file renaming tool
# this script will have functionality
# create any given amt of text files and
# place them in a particular folder. This script
# will also alow you to create a folder if one
# that is named does not already exist.

# The inspiration for this came from a question I saw
# on Stack and I saw a couple of UpWork gigs that needed 
# this kind of service provided.

# I will link all of my resources in the README
# as well as any and all links I used to copy
# code from. 
#.......................................................


from os import(
    path, makedirs, listdir
)
from sys import (
    argv, exit)

def get_next_available_filename(folder):
    i = 1
    while True:
        filename = path.join(folder, f"file{i}.txt")
        if not path.exists(filename):
            return filename
        i += 1

def create_text_files(num_files, folder):
    if not path.exists(folder):
        makedirs(folder)

    starting_index = len(listdir(folder)) + 1

    for i in range(starting_index, starting_index + num_files):
        filename = get_next_available_filename(folder)
        with open(filename, "w") as file:
            file.write("This is the content of file {}.".format(i))
        print("Created", filename)

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python script.py <num_files> <folder>")
        exit(1)

    num_files = int(argv[1])
    folder = argv[2]

    create_text_files(num_files, folder)