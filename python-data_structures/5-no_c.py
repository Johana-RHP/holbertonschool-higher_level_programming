#!/usr/bin/python3
def no_c(my_string):
    new_string_1 = my_string.translate({ord('c'): None})
    new_string_2 = new_string_1.translate({ord('C'): None})
    return new_string_2
