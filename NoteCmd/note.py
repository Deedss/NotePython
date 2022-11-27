#!/usr/bin/python
# This will be a note taking application on the commandline written fully in Python
import argparse
import os
from datetime import datetime


def writeNote(parsed_args):
    full_name = parsed_args.get(
        "directory") + "/" + parsed_args.get("filename") + parsed_args.get("extension")
    os.system('%s %s' % (os.getenv('EDITOR'), full_name))


def read():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', default=os.getcwd(),
                        help='input the file location, default is current directory')
    parser.add_argument('-f', '--filename', default=time_date(),
                        help='file name for the note, default is timedate')
    parser.add_argument('-e', '--extension', default=".txt",
                        help='the file extension, default is .txt')
    args = parser.parse_args()
    return vars(args)


def time_date():
    now = datetime.now()
    dt_string = now.strftime("%b-%d-%Y-%H:%M")
    return dt_string


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError("readable_dir:{path} is not a valid path")


def main():
    print("Hello World")
    x = 5
    y = 10
    temp = [1, 2, 3, 4, 5]
    print(temp)
    print(x + y)
    print(x % y)
    print(x / y)


if __name__ == '__main__':
    main()
