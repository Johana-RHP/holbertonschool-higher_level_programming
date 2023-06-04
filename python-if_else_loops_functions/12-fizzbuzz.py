#!/usr/bin/python3
def fizzbuzz():
    for number in range(1,101):
        if number == 100:
            print(f"Buzz", end="")
        elif number % 15 == 0:
            print(f"FizzBuzz", end=" ")
        elif number % 3 == 0:
            print(f"Fizz", end=" ")
        elif number % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")
