#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = len(argv)
    if length == 1:
        print(f"{0} arguments.")
    elif length == 2:
        print(f"{1} argument:")
    elif length > 2:
        print("{:d} arguments:".format(length - 1))
    for number in range(1, length):
        print("{:d}: {}".format(number, argv[number]))
