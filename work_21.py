import datetime

class Car:
    def __init__(self, factory: str, brand: str, fealue_consaltion: float, year=2020):
        self.factory = factory
        self.brand = brand
        self.year = year
        self.melage = 0
        self.fealue_consaltion = fealue_consaltion

    def __str__(self) -> str:
        return f'Car: {self.factory} {self.brand}, {self.year}, {self.melage}'

    __repr__ = __str__

    @property
    def age(self) -> int:
        my_age = (datetime.datetime.today().year - self.year)
        return my_age


bmw = Car('bmw', 'x5', 100.0, 1999)
audi = Car('audi', 'x10', 100.0, 1999)
print(bmw.age)
print(bmw.__dict__)
