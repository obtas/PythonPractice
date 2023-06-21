string_example1 = 'This is an example'

string_example2 = "This is also an example"

string_example3 = """This is also a string example
on more than one line.
Triple double quotes allow you to do so"""

s = "PYTHON"
print('Entire string =', s)
print('1st character =', s[0])
# print the first 2 characters (index 0 to 1)
print('Sliced character =', s[0:2])

# string formatting character %
# prints Today I have eaten 3 apples
print('Today I have eaten %d apples' %3)

# can use %d to format integers. Can use %s to format text

# concatenate using +
example = "Today is" + " " + "a wonderful day"
print(example)

# multiply strings using *
# prints Yes Yes Yes Yes
example2 = "Yes " * 4
print(example2)

# append using +=
# string will be added at the end
example3 = "Today is a beautiful day "
example3 += "to start learning python"
print(example3)

# find length of string using len()
print(len(example3))

# find() provides the index for the position the first time the input is found
# prints 9
# if substring is not found, the interpreter will return a value of -1
x = "Tomorrow it will be sunny"
y = x.find('it')
print(y)

# lower() and higher() functions can be used to convert characters in a string
# to completely lower or upper case.

example4 = "Asia is the biggest continent"
sample = example4.lower()
print(sample) 
sample2 = example4.upper()
print(sample2)

# title() converts to camel case format
sample3 = example4.title()
print(sample3)