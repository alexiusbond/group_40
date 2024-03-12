class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        if type(address) == Contact:
            self.__address = address
        else:
            raise TypeError('The field address must be a Contact')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Invalid age, it must be an integer')

    def info(self):
        return (f'CONTACT INFO: {self.__address.city}, {self.__address.street} '
                f'{self.__address.number}\n'
                + f'{self.__name} is {self.__age} years old. '
                  f'Birth year is {2024 - self.__age}.')

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, commands, address):
        super(Dog, self).__init__(name, age, address)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def __del__(self):
        print(f'{self.get_name()} is deleted')

    def info(self):
        return super().info() + f' Dog knows: {self.__commands} commands.'

    def speak(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, address):
        super(FightingDog, self).__init__(name, age, commands, address)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f' It has {self.__wins} of wins.'

    def speak(self):
        print('Rrrrr gav')


class Cat(Animal):
    def __init__(self, name, age, address):
        super(Cat, self).__init__(name, age, address)

    def speak(self):
        print('Myau')


class Fish(Animal):
    def __init__(self, name, age, address):
        super(Fish, self).__init__(name, age, address)


# some_animal = Animal('Anim', 2)
# some_animal.__age = 'Five'
# some_animal.set_age(3)
# print(some_animal.info())
# print(some_animal.get_name())


contact_1 = Contact('Bishkek', 'Isanova', 3)

cat = Cat('Garfield', 4, contact_1)
# print(cat.info())

dog = Dog('Bob', 5, 'Sit', contact_1)
dog.commands = 'Sit, bark'
# print(dog.commands)
# print(dog.info())

# contact_2 = Contact('Osh', 'Bonieva', 1)
#         a = b

fightingDog = FightingDog('Tyson', 1, 'Fight, bite', 9,
                          Contact('Osh', 'Bonieva', 1))
# print(fightingDog.info())

# contact_1.number = 5
# print(cat.info())
# print(dog.info())

fish = Fish('Nemo', 2, contact_1)

animals_list = [fish, cat, dog, fightingDog]
for animal in animals_list:
    print(animal.info())
    animal.speak()
