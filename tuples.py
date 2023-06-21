t = ('Cat', 'Tree', 'Apple')

# cannot replace elements in tuples

tuple1 = (17,18,19)
tuple2 = (16,19,28)

# prints (17, 18, 19, 16, 19, 28)
print(tuple1 + tuple2)

# Nested tuples
x = (1,2,3)
y = ('orange', 'apple', 'banana')
z = (x,y)

# prints ((1, 2, 3), ('orange', 'apple', 'banana'))
print(z)

# replication
a = x * 4

# prints (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(a)

# can slice tuples
print(a[2:4])

# cannot delete specific elements from a tuple but can delete tuple using del
del a
print(a)