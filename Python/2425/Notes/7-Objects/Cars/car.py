class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def description(self):
        return(f"\n\tMake: {self.make}\n\tModel: {self.model}\n\tYear: {self.year}\n\tColor: {self.color}\n")
