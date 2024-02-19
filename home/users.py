class bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class newbank(bank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class control:
    def __init__(self, name, age, money, key, property1, property2, property3):
        self.bank = bank(name, age, money, key)
        self.property1 = property1
        self.property2 = property2
        self.property3 = property3

    def set_property1(self, property1):
        self.property1 = property1

    def get_property1(self):
        return self.property1

user = control("john", 30, 10000, "1234", "house", "car", "business")

user.bank.set_name("smith")
user.set_property1("apartment")

with open("users.txt", "w") as file:
    file.write(f"name: {user.bank.get_name()}\n")
    file.write(f"age: {user.bank.get_age()}\n")
    file.write(f"money: {user.bank._bank__money}\n")
    file.write(f"key: {user.bank._bank__key}\n")
    file.write(f"property1: {user.get_property1()}\n")
    file.write(f"property2: {user.property2}\n")
    file.write(f"property3: {user.property3}\n")
