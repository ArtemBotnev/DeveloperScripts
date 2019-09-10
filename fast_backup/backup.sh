#!/bin/bash

# Created by Artem Botnev on 09/09/2019

# Requires python version 3.5 or higher
# Copies all new and updated source directory files to destination directory
# (checks if each file already exist in destination directory and copy only if
# it doesn't or has been updated)
# Copies full directories tree
# Exclude empty folders

# example of usage:

# ./backup.sh ~/source ~/dist
# will copy -> subdirectories with files from ~/source to ~/dist

python3 backup.py $1 $2