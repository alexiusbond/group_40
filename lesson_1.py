class Transport:
    def __init__(self, the_model, the_color, the_year):
        self.model = the_model
        self.color = the_color
        self.year = the_year

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_color, the_year):
        super().__init__(the_model, the_color, the_year)


class Car(Transport):
    counter = 0
    standard_number_of_wheels = 4

    # constructor           # parameters
    def __init__(self, the_model, the_color, the_year, penalties=0):
        # fields / attributes
        super().__init__(the_model, the_color, the_year)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    standard_number_of_wheels = 12
    def __init__(self, the_model, the_color, the_year, penalties=0, load_capacity=0):
        super().__init__(the_model, the_color, the_year, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type_of_product, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded {type_of_product} '
                  f'({weight} kg.) on truck {self.model}')


print(f'Fabric CAR produced: {Car.counter} cars.')
price_of_lastic = 5000
print(f'We need {price_of_lastic * Car.standard_number_of_wheels * Car.counter} soms.')

number = 9
bmw = Car('BMW X6', 'red', 2020)
print(bmw)
print(f'MODEL: {bmw.model} COLOR: {bmw.color} YEAR: {bmw.year} PENALTIES: {bmw.penalties}')

honda = Car(the_year=2009, the_model='Honda Fit', the_color='blue', penalties=1000)
print(f'MODEL: {honda.model} COLOR: {honda.color} '
      f'YEAR: {honda.year} PENALTIES: {honda.penalties}')
# honda.color = 'silver'
honda.change_color('silver')
print(f'MODEL: {honda.model} NEW COLOR: {honda.color} '
      f'YEAR: {honda.year} PENALTIES: {honda.penalties}')
honda.drive('Osh')
honda.drive('Batken')
bmw.drive('Kant')

print(f'Fabric CAR produced: {Car.counter} cars.')
print(f'We need {price_of_lastic * Car.standard_number_of_wheels * Car.counter} soms.')

boeing = Plane('Boeing 747', 'white', 2023)
print(f'MODEL: {boeing.model} COLOR: {boeing.color} YEAR: {boeing.year}')

scania = Truck('Scania 300', 'green',
               2019, 900, 35000)
print(f'MODEL: {scania.model} COLOR: {scania.color} '
      f'YEAR: {scania.year} PENALTIES: {scania.penalties} '
      f'LOAD CAPACITY: {scania.load_capacity} kg')
scania.load_cargo('apples', 40000)
scania.load_cargo('oranges', 20000)
scania.drive('Karakol')

print(f'By standard truck has {Truck.standard_number_of_wheels} wheels.')