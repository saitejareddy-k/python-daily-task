# Creating a Car class

class Car:

    # Constructor
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    # Method to display car details
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Color:", self.color)
        print("Car Model:", self.model)

    # Method to start the car
    def start(self):
        print("The car is starting...")

    # Method to stop the car
    def stop(self):
        print("The car is stopping...")


# Creating objects
car1 = Car("BMW", "Black", "X5")
car2 = Car("Audi", "White", "A6")

# Calling methods
print("First Car Details:")
car1.display()
car1.start()
car1.stop()

print("\nSecond Car Details:")
car2.display()
car2.start()
car2.stop()
