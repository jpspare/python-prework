# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    """Prints a username"""
    print("hello_" + user_name)


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and 
# returns nothing
def first_odds():
    """Prints the odd numbers between 1 and 100"""
    for i in range(50):
        i = i * 2 + 1
        print(i)
    return


# Question 3
# Please write a Python function, max_num_in_list to return the max number of 
# a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Returns the maximum number in a list."""
    if isinstance(sorted(a_list)[-1],int):
        return sorted(a_list)[-1]
    else:
        return "Please provide a list of numbers."


# Question 4
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Determines whether a given year is a leap year."""
    if a_year % 4 != 0:
        return False
    elif a_year % 100 == 0 and a_year % 400 != 0:
        return False
    else:
        return True


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
# consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Determines whether a list of integers is consecutive"""
    if sorted(a_list) == list(range(min(a_list),max(a_list)+1)):
        return True
    else:
        return False
