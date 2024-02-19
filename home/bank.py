class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class NewBank(Bank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Control:
    def __init__(self, name, age, money, key, property1, property2, property3):
        self.bank = Bank(name, age, money, key)
        self.property1 = property1
        self.property2 = property2
        self.property3 = property3

    def set_property1(self, property1):
        self.property1 = property1

    def get_property1(self):
        return self.property1


control = Control("John", 30, 10000, "1234", "house", "car", "business")
control.bank.set_name("Smith")
control.set_property1("apartment")

with open("users.txt", "w") as file:
    file.write(f"Name: {control.bank.get_name()}\n")
    file.write(f"Age: {control.bank.get_age()}\n")
    file.write(f"Money: {control.bank._Bank__money}\n")
    file.write(f"Key: {control.bank._Bank__key}\n")
    file.write(f"Property1: {control.get_property1()}\n")
    file.write(f"Property2: {control.property2}\n")
    file.write(f"Property3: {control.property3}\n")

# Code for "eni.py" file:
import turtle

# Turtle drawing code here

# Code to read and print text file content
with open("users.txt", "r") as file:
    content = file.read()
    print(content)

