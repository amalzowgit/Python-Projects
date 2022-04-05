def say_hi(name): # define function say_hi()
    if name == '': # if no name is entered, print reprimand
        print("You didn't enter your name!")
    else: # else greet user by listing one letter at a time on a new line
        print("Hi there...")
        for letter in name:
            print(letter)

# ask for name input
name = input("Your name: ")

# now the pogram says hi
say_hi(name)
