class Dog:
    def __init__(self, name, age): #constructor. It is automatically called when an instance (object) of a class is created. The purpose is to initialize the attributes of the newly created object.
        self.name = name #Using "self" makes it immediately clear to anyone reading the code that the method is referring to the instance of the class.
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def get_age(self):
        return self.age

# Creating an instance of the Dog class
dog1 = Dog("Buddy", 3)

# Calling instance methods
dog1.bark()  # Output: Buddy says woof!
print(dog1.get_age())  # Output: 3
