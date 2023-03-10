"""Exercise Two:
Create a program that asks the user for two numbers and checks if the first number is 
equal to, greater than, or less than the second number. Print the results of each comparison.
"""

# def choose_number():
#     a = int(input("choose your first number: "))
#     b = int(input("choose your second number: "))

#     if a > b:
#         print(a," is greater than ",b)
#     elif a < b:
#         print(a," is less than ", b)
#     else:
#         a == b
#         print(a, " is equal to ",b)


"""Exercise Three:
Create a program that asks the user for three numbers and checks if all of them are positive, or at least one of them
is negative. Print the result of the logical operation.
"""

# a = int(input("choose your first number: "))
# b = int(input("choose your second number: "))
# c = int(input("choose your third number: "))

# def check_number():
#     if a > 0 and b > 0 and c > 0:
#         print("All of your values are positive")
#     else:
#         print("One of your values is negative")

# check_number()

"""Exercise Four:
Create a program that asks the user for three numbers and check for each number if it is divisible by 3, 4 or 7. 
Print the result each time
"""

# a = int(input("choose your first number: "))
# b = int(input("choose your second number: "))
# c = int(input("choose your third number: "))

# def is_divisible_by():
#     if (a % 3 == 0) or (a % 4 == 0) or (a % 7 == 0):
#         print(a, "can be divided by 3, 4 or 7")
#         print(a, "divided by 3 is", a // 3)
#         print(a, "divided by 4 is", a // 4)
#         print(a, "divided by 7 is", a // 7)
#         print("-" * 50)
#     if (b % 3 == 0) or (b % 4 == 0) or (b % 7 == 0):
#         print(b, "can be divided by 3, 4 or 7") 
#         print(b, "divided by 3 is", b // 3)
#         print(b, "divided by 4 is", b // 4)
#         print(b, "divided by 3 is", b // 7)
#         print("-" * 50)
#     if (c % 3 == 0) or (c % 4 == 0) or (c % 7 == 0):
#         print(c, "can be divided by 3, 4 or 7")
#         print(c, "divided by 3 is", c // 3)
#         print(c, "divided by 4 is", c // 4)
#         print(c, "divided by 7 is", c // 7)
#         print("-" * 50)
#     else:
#         print("These numbers cannot be divided by 3, 4 or 7")

# is_divisible_by()

"""Exercise Five:
Write a program that the user to input two numbers and then performs both a modulus and floor division
operation on those numbers. Print the results of both operations to the screen.
"""

def modulus_number():
    a = int(input("choose your first number: "))
    b = int(input("choose your second number: "))

    c = a % b
    d = a // b

    print("modulus operation result: ", c)
    print("floor division operation result: ", d)

modulus_number()