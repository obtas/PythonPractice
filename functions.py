"""Exercise One:
Create a function that takes two numbers as parameters, and returns the result of the sum of both
numbers."""

def sum_of_numbers(num1, num2):
    num3 = num1 + num2
    print(num3)

# sum_of_numbers(5, 3)

"""Exercise Two:
Create a function that takes a string as a parameter, and returns the number of vowels in the string."""

def no_of_vowels(string):
    vowels = 'aeiouAEIOU'

    count = 0

    for char in string:
        if char in vowels:
            count += 1
        else:
            pass
    
    print(f'The number of vowels in {string} is {count}')

# no_of_vowels('unequivocally')
    
"""Exercise Three:
Create a function that takes two strings as parameters and returns a message indicating if both strings
are equal or not."""

# str1 = input("Please enter the first string: ")
# str2 = input("Please enter the second string: ")

def string_checker(str1, str2):
    if str1 == str2:
        print("The strings are equal")
    else:
        print("The strings are not equal")

# string_checker(str1, str2)

"""Exercise Four:
Create a function that takes a number as a parameter, and returns a message indicating if the number
is positive, negative or zero"""

def number_checker(num):
    if num == 0:
        return "The number you have entered is zero"
    elif num > 0:
        return "The number you have entered is positive"
    else:
        return "The number you have entered is negative"

number = int(input("Enter a number: "))
result = number_checker(number)
# print(result)

"""Exercise Five:
Create a module with a function that takes a list as a parameter and returns the sum of all elements in
the list. Import this module into another script and use the function to sum a list of numbers."""

import function_module

x = (1,2,3,4,5)

print(function_module.sum_of_list(x))

