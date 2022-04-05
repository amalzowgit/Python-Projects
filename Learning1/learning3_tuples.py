# https://python.land/python-data-types/python-tuple
# tuples

# optional parentheses
my_numbers = (1, 2, 3)
the_same = 1, 2, 3
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)

# Like everything in Python, tuples are objects and have a class that defines them

tuple([0,1,2])

# Python will reduce the following expression to just 1
t = (1)

# to let Python know we're creating a tuple with one element by using a comma:
t = (1, )

# The leading * operator unpacks the lists into individual elements. 
# It’s as if you would have typed them individually at that spot. 
# This unpacking trick works for all iterable types if you were wondering!
l1 = [1, 2, 3]
l2 = [4, 5, 6]
t = (*l1, *l2)
t

# unpacking tuples
person = ('Angela', 37, True)
name, age, registered = person
name

# great to use with a function that returns multiple values
def get_user_by_id(userid):
    #fetch user from database
    #....
    return name, age

name, age = get_user_by_id(4)

# access tuples using index #s
my_mixed_tuple = 'Hello', 123, True
my_mixed_tuple[0]
# 'Hello'
my_mixed_tuple[2]
# True

# Because a tuple is immutable, you can not append 
# data to a tuple after creating it
# You can, of course, create a new tuple from the old 
# one and append the extra item(s) to it this way:
t1 = (1, 2, 3)
t = (*t1, 'Extra', 'Items')
t
# (1, 2, 3, 'Extra', 'Items')
# What we did was unpack t1, create a new tuple with 
# the unpacked values and two different strings and 
# assign the result to t again.

t = 1, 2, 3
len(t)
# 3

# diff from LISTS
# since a tuple is immutable - it cannot be changed or added to
# this can be viewed as a type of 'write protection'
# it can prevent mistakes
# tuples are faster than lists
# simple array-like structure

# diff from SETS
# tuples can have duplicates, sets cannot

# convert tuple to list using list() constructor
t = 1, 2, 3
list(t)

# another, less simple way, is to unpack
# handly when unpacking mult tuples or adding extra values
t = 1, 2, 3
l = [*t]
l

l = [*t, 4, 5, 6]
l

# convert tuple to set
t = (1, 2, 3)
s = set(t)
s
# {1, 2, 3}

# unpacking technique
s = {*t}
s
# {1, 2, 3}

# convert tuple to string
t = (1, 2, 3)
print(t)
# (1, 2, 3)
str(t)
# '(1, 2, 3)'




