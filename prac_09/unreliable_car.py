from car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.

        name: string, name of the car
        fuel: float, one unit of fuel drives one kilometre
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.uniform(1, 100) < self.reliability:
            super().drive(distance)
        return distance
