class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def showInfo(self):
        return f"Hello {self.name}"
    
    def age_in_days(self):
        return f"Your age in days is {self.age * 365}"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
p1 = Person(name,age)

print(p1.showInfo())

print(p1.age_in_days())
