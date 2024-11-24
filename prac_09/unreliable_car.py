from car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.

        name: string, name of the car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.uniform(1, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        return distance
