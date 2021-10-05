#!/usr/bin/env python
# This will be a note taking application on the commandline written fully in Python
import os
import argparse
from datetime import datetime

def read():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', default=os.getcwd() , type=dir_path, help='input the file location, default is current directory') 
    parser.add_argument('-f', '--filename', default=time_date() , help='file name for the note, default is timedate')
    parser.add_argument('-e', '--extension', default=".txt", help='the file extension, default is .txt')
    args = parser.parse_args()
    print(args)

def time_date():
   now = datetime.now()
   dt_string = now.strftime("%b-%d-%Y-%H-%M")
   return dt_string

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def main():
    read()

if __name__ == '__main__':
    main()
