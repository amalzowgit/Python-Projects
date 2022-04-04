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

