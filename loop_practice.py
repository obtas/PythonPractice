"""Exercise One:
Write a program that asks the user for an integer and calculates the factorial of the given number. 
Use a for loop to accomplish this task"""

a = int(input("Enter a number: "))
factorial = 1

for i in range(1, a+1):
    # *= means factorial times i
    factorial *= i

print("The factorial of", a, "is", factorial)

"""Exercise Two:
Write a program that counts the number of vowels (a, e, i, o, u) of a string given as input from the user. 
Loop the string and check if the character is a vowel"""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for letters in text:
    if letters in vowels:
        count += 1

print("The number of vowels in the string is: ", count)

"""Exercise Three:
Create some code to produce a random number between 1 and 100. The program should then ask the
user to guess the number, and keep asking until the user has entered the correct number. Use a while
loop to accomplish this task."""

import random

rand_num = random.randint(1,10)

input_num = int(input("Guess the number: "))

while input_num != rand_num:
    if input_num < rand_num:
        print("Too low")
        print("Incorrect! Guess again")
    else:
        print("Too high")
        print("Incorrect! Guess again")
    input_num = int(input("Guess the number: "))
if input_num == rand_num:
    print("Well done! You guessed correctly. The correct number is", rand_num)

"""Exercise Four:
Write a program that prints the first n even numbers. Ask the user for the value of n. Use a for loop to
generate the numbers, and an if statement to determine if the current number is even"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

"""Exercise Five:
Write a program that prints the first n Fibonacci numbers. The Fibonacci sequence is a series of
numbers in which each number is the sum of the two preceding ones. The first two numbers in the
series are 0 and 1. Use a for loop to generate the numbers and break the loop when n numbers have
been printed."""

n = int(input("Enter the number of fibonacci numbers to generate: "))

fib = [0, 1]

for i in range(2, n):
    print(i)
    next_num = fib[i-1] + fib[i-2]
    fib.append(next_num)

print("The first", n, "Fibonacci numbers are:", fib[:n])
