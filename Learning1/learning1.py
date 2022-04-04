Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
if ready:
    print("Let's start learning Python programming")

    
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    if ready:
NameError: name 'ready' is not defined
def bigger_than_five(x):
  # The contents of a function are indented
  if x > 5:
    # This is another, even more indented block of code
    print("X is bigger than five")
  else:
    # And one more!
    print("x is 5 or smaller")

    

def bigger_than_five(x):
  if x > 5:
    print("X is bigger than five")
  else:
    print("x is 5 or smaller")

    
x = 6
print(bigger_than_five)
<function bigger_than_five at 0x000001C169B2BEB0>

def bigger_than_five(x):
    if x > 5:
        print("X is bigger than five!")
    else:
        print("x is smaller than five.")

print(1+3)
4

a = 6 + 9
print(a)
15
mystring = "It's a string, with a single quote!"
print(mystring)
It's a string, with a single quote!
mystring2('It's a string, with a single quote!'
          
SyntaxError: unterminated string literal (detected at line 1)
mystring2 = 'It\'s an escaped quote!'
          
print(mystring2)
          
It's an escaped quote!
mystring3 = "I'm a so-called \"script kiddie\""
          
mystring3
          
'I\'m a so-called "script kiddie"'
mybigstring = """This is line 1,
this is line 2,
this is line 3."""
          
mybigstring
          
'This is line 1,\nthis is line 2,\nthis is line 3.'
print(mybigstring)
          
This is line 1,
this is line 2,
this is line 3.
line = """Sally sold seashells: by the seashore "Yes", she said."""
          
line
          
'Sally sold seashells: by the seashore "Yes", she said.'
mystrong = "Hello World"
          
mystring = "Hello World"
          
mystring.lower()
          
'hello world'
mystring.upper()
          
'HELLO WORLD'
len("I wonder how long this string will be...")
          
40
len(mystring)
          
11
'Hello world'.split(' ')
          
['Hello', 'world']
'Hello \t\n there, \t\t\t stranger.'.split()
          
['Hello', 'there,', 'stranger.']
'Hello world'.replace('H', 'h')
          
'hello world'
'Hello world'.replace('l', '_')
          
'He__o wor_d'
'Hello world'.replace('world', 'readers')
          
'Hello readers'
mystring = 'Hello world'
          
mystring[2]
          
'l'
mystring[0]
          
'H'
mystring[::-1]
          
'dlrow olleH'
my_age = 40
          
f'My age is {my_age}'
          
'My age is 40'
f''3+4 = {3 + 4}'
          
SyntaxError: unterminated string literal (detected at line 1)
f'3 + 4 = {3 + 4}'
          
'3 + 4 = 7'
my_age = 37
          
f'My age is, unfortunately, not {my_age-8}'
          
'My age is, unfortunately, not 29'
