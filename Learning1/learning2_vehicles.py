Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print('Halting')

        
car = Car()
car.increase_speed(10)
SyntaxError: multiple statements found while compiling a single statement
car = Car()
car.increase_speed(10)
You need to start the car first
car.start()
Car started, let's ride!
car.incre
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    car.incre
AttributeError: 'Car' object has no attribute 'incre'
car.increase_speed(10)
Vrooooom!

car1 = Car()
car2 = Car()
id(car1)
2479631981328
id(car2)
2479631981232
car1.start()
Car started, let's ride!
car1.increase_speed(10)
Vrooooom!
car1.speed
10
car2.speed
0

'a' + str(1)
'a1'
int('2') + 2
4

class Car:
    def __init__(self, started = False, speed = 0)
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed +delta
            print('Vrooooom!')
        else:
            print("You need to start the car first.")

    def stop(self):
        self.speed = 0
        print('Halting!')
        
SyntaxError: expected ':'


class Car:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed +delta
            print('Vrooooom!')
        else:
            print("You need to start the car first.")

    def stop(self):
        self.speed = 0
        print('Halting!')

        
car1 = Car()
car2 = Car(True)
car3 = Car(True, 50)
car4 = Car(started = True, speed=40)

dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first!")

            
class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

        
class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start(self):
        print("Sorry, out of fuel!")

        
car1 = Car()
car2 = Car()
mtrcycl1 = Motorcycle()
mtrcycl2 = Motorcycle()
car1.start()
Started, let's ride!
mtrcycl1.start()
Sorry, out of fuel!

type(3)
type('hello')
type([1,2,3])
SyntaxError: multiple statements found while compiling a single statement
type(3)
type('hello')
type([1,2,3])
SyntaxError: multiple statements found while compiling a single statement

type(3)
<class 'int'>
type('hello')
<class 'str'>
type([1,2,3])
<class 'list'>
int('100')
100
str(100)
'100'
int(2.3)
2
import random
random.randint(1,10)
3
type(2)
<class 'int'>
if isinstance(2, int):
    print('An integer')

    
An integer
