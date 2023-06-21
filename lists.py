# Lists

list1 = [22,23,24]
list2 = ["Alaska", "California", "Alabama"] 

print(list2)

empty_list = []

print(list2[0])
print(list2[1])
print(list2[2])

print(list2[0] + " is a wonderful state")

x = [[5,123, 4], 56, 32, 14]
print(x)
print(x[0][1])

# Slicing lists
# syntax - Listname[start of the index : end of the index]
print(list1[0:1])

my_list = [23,34,78,94,54]
# prints 23,34,78
print(my_list[:3])

# prints 94,54
print(my_list[3:])

# prints whole list
print(my_list[:])

# changing values of list
my_list[3] = 58
print(my_list)

# replacing a list value with an already existing list value
my_list[3] = my_list[2]
print(my_list)

# concatenating lists
# prints [23, 34, 78, 78, 54, 1, 2, 3]
a = [1,2,3]
print(my_list + a)

# replicating lists
# prints [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(a * 4)

# deleting elements
# prints [12, 13, 15, 16, 17]
my_second_list = [12, 13, 14, 15, 16, 17]
del(my_second_list[2])
print(my_second_list)

# in and not in operators
# True 
colours = ["yellow","orange", "blue"]
b = "orange" in colours
print(b)

# index() function determinds the index position of a list element
c = [12, 45, 78]
print(c.index(45))

# insert() can insert new elements into a list
# insert(index position, "item")
d = [12,45,78]
d.insert(2,11)
print(d)

# sort() sorts list either in ascending or descending order, with strings will be ordered alphabetically
e = [78, 12, 45, 67]
e.sort()
print(e)

f = ["orange", "black", "purple", "yellow", "blue"]
f.sort()
print(f)