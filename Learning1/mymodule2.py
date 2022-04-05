# https://python.land/project-structure/python-modules
# The If __name__ == '__main__' check

def greeter():
    print("Hello from mymodule.py")

# Only call the greeting when run as
# a script (with python mymodule.py)

if __name__ == '__main__':
    greeter()
