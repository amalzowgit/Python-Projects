Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello, readers!')
Hello, readers!
print(15)
15
result = print('Hello')
Hello
print(result)
None
# len() to return the length
mylength = len('Hello')
print(mylength)
5
# ref: https://python.land/introduction-to-python/functions
# Creating a Python function
def say_hi():
    print('Hi!')

    
say_hi()
Hi!

# Python function with multiple arguments
def welcome(name, location):
    print("Hi ", name, "welcome to ", location)

    
welcome('Angela', 'this tutorial.')
Hi  Angela welcome to  this tutorial.
#it looks like I don't need to add extra spaces

Returning values
SyntaxError: invalid syntax
#Returning values
def add(a, b):
    return a + b

result = add(10, 15)
print(result)
25

if add(1, 1) == 2:
    print("That's what you'd expect!")

    
That's what you'd expect!

# mpty return statement
def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :P
        return

    
def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :P
        return

    
print('Hi there, ', name)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('Hi there, ', name)
NameError: name 'name' is not defined
def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :P
        return
    print('Hi there, ', name)

    
optional_greeter('Xander')
def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :P
        pass
    else:
        print('Hi there, ', name)

        
optional_greeter('Xander')

# The visibility of a variable is called scope.
def say_hi():
    print("Hi", name)
    answer = "Hi"

    
name = 'Angela'
say_hi()
Hi Angela
print(answer)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(answer)
NameError: name 'answer' is not defined
# answer is defined inside say_hi() function and it not known outside of the function thus causes NameError

#Default values and named parameters
#A compelling Python feature is the ability to provide default values for the parameters:

def welcome(name='learner', location='this tutorial'):
    print('Hi', name, "welcome to", location)

    
welcome()
Hi learner welcome to this tutorial
welcome(name='Angela')
Hi Angela welcome to this tutorial
welcome(location='this amazing tutorial')
Hi learner welcome to this amazing tutorial
welcome(name='Angela', location='this amazing tutorial.')
Hi Angela welcome to this amazing tutorial.

def welcome(name='learner', location='this tutorial'):
    print("Hi", name, "welcome to", location)

    
welcome('Angela', 'your home')
Hi Angela welcome to your home
