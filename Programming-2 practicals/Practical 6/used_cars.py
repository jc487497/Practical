"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac6.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Audi",180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    limo = Car("Mercedes", 100)
    print("fuel= ", limo.fuel)
    limo.drive(115)
    print("odo = ", limo.odometer)
    print(limo)

main()

