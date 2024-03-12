from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    BLUE = '\33[34m'
    GREEN = '\33[32m'


class Drawable():
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    # def __init__(self)
    #     pass
    def play_music(self, song):
        print('Playing ' + song)

    def stop_music(self):
        print('Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return (f'MODEL: {self.__model}, YEAR: {self.__year}, COLOR: '
                f'{self.__color.value}{self.__color.name}') + '\33[0m'

    def __gt__(self, other):
        return self.__year > other.__year

    def __le__(self, other):
        return self.__year <= other.__year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return f'AI - 98'

    @classmethod
    def get_fuel_amount(cls):
        return cls.__total_fuel_amount

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel_amount += amount

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel.')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using electric.')

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


# some_car = Car('Ford Focus', 2000, 'red')
# print(some_car)

print(f'FABRIC FUEL CAR has: {FuelCar.get_fuel_amount()} litters of fuel.')

ford_car = FuelCar('Ford Mustang', 2022, Color.RED, 60)
print(ford_car)

tesla_car = ElectricCar('Model S', 2023, Color.BLUE, 25000)
print(tesla_car)

toyota_car = HybridCar('Toyota Camry',
                       2024, Color.GREEN, 50, 15000)
toyota_car.drive()
print(toyota_car)

print(HybridCar.mro())

number_1 = 8
number_2 = 10
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Number one is smaller than number two: {number_1 < number_2}')
print(f'Ford is better than Toyota: {ford_car > toyota_car}')
print(f'Ford is worse or the same than Toyota: {ford_car <= toyota_car}')

print(number_1 + number_2)
print(ford_car + toyota_car)

# FuelCar.total_fuel_amount -= 100
FuelCar.buy_fuel(500)
print(f'FABRIC FUEL CAR has: {FuelCar.get_fuel_amount()} litters ({FuelCar.get_fuel_type()}) of fuel.')

tesla_car.play_music('Best song')

samsung = SmartPhone()
samsung.play_music('Song 1')
samsung.draw('📱')
tesla_car.draw('🚗')

if tesla_car.model == 'Model-S':
    print('This car is cool')

if tesla_car.color == Color.BLUE:
    print('This car is beautiful')
