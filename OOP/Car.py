class Car:
    def __init__(self, make, model, color, year): # constructor
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def move(self):
        print('Moving')

    def brake(self):
        print('Braking')
