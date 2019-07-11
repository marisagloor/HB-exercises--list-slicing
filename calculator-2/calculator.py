"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


    # repeat forever:
while True:
    # read input
    user_input = input('> ')
    # tokenize input
    tokens = user_input.split(" ")
    # if the first token is "q":
    #     quit
    if tokens[0] == 'q':
        break
    # else:
    #     decide which math function to call based on first token
    elif tokens[0] == '+':
        print(add(tokens[1:]))
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == 'square':
        print(square(float(tokens[1])))
    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))
    elif tokens[0] == 'pow':
        print(power(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))
    else: 
        print('Error! Please try again.')

print('Goodbye!')