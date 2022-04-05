def say_hi(name): # define function say_hi()
    if name == '':
        print("You didn't enter your name!")
    else:
        print('Hi there...')
    for letter in name:
        print(letter)

while True:
    # Ask for name first using input()
    name = input('Your name: ')
    # And then call say_hi with that name
    say_hi(name)
