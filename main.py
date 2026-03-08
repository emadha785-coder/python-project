class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def showInfo():
        return f"Hello {self.name}"

name = input("Enter your name: ")
age = int(input("Enter your age: ")

p1 = Person(name,age)

print(p1.showInfo())
