#!/usr/bin/python3
"""a function that prints a text with 2 new lines"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    k = 0
    while k < len(text) and text[k] == ' ':
        k += 1

    while k < len(text):
        print(text[k], end="")
        if text[k] == "\n" or text[k] in ".?:":
            if text[k] in ".?:":
                print("\n")
            k += 1
            while k < len(text) and text[k] == ' ':
                k += 1
            continue
        k += 1
