# For loops
# great for automating tasks

v = [45, 89, 56]

out = 0

for val in v:
    out = out + val

print("Sum of the 3 elements of the vector v:", out)

# While loop

a = 0
b = 1

N = int(input("Enter number: "))

while b <= N:
    a = a + b
    b = b + 1
print("The sum of the numbers from 1 to", N, "is", a)

# Break - ends the loop and moves on to the line following the loop. 
# Any time the break occurs inside a loop, the loop will end and the next statements will be executed.

# Continue - immediately ends the loop and moves onto the next iteration. 

for letter in 'Productivity':
    if letter == 't':
        continue
    print('Letter now: ', letter)

    