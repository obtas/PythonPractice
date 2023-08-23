"""Exercise one:
Create a list of 5 numbers and then print the sum and average of the numbers"""

numbers = [1,2,3,4,5]

print(sum(numbers))
print(sum(numbers)//len(numbers))

"""Exercise Two:
Create a tuple of 5 names and then print the first and last name"""

tuple = ('Samantha Kelly', 'Dave Smith', 'Tim Hughes', 'Betty Benedict', 'Nicki Stevens')
print(tuple)

"""Exercise Three:
Create a dictionary with 5 key-value pairs and then print the value of the third key."""

dictionary = {"NCT 127":"9 members", "WayV": "5 members", "NCT Dream":"6 members", "aespa": "4 members", "NCT U": "21 members"}
print(dictionary["NCT Dream"])

"""Exercise Four:
Create a list with 5 fruits. Ask the user to input a fruit. Check if the fruit is in the list. 
If the fruit is in the list. If the fruit is in the list, display a message saying "The fruit is in the list."
If the fruit is not in the list, display a message saying "The fruit is not in the list." """

fruit = ['Banana', 'pear', 'grapes', 'strawberry', 'apple']

a = input("Name a fruit: ")

if a in fruit:
    print("The fruit is in the list.")
else:
    print("The fruit is not in the list.")


"""Exercise Five:
Create a list with 3 colours. Then ask the user to give a colour as input. If the colour is in the list, display a message saying so.
Otherwise, append the colour given by the user to the end of the list and print the updated list."""

colour = ['purple', 'red', 'black']

a = input("Name a colour: ")

if a in colour:
    print("This colour is in the list.")
else:
    colour.append(a)
    print(colour)