#!/usr/bin/env python3

# Declare the global list before function definitions
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return the entire list unchanged
    return my_list

def give_first_item():
    # Return the first item as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Return a list containing first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return a list containing second and third items
    return my_list[1:3]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
