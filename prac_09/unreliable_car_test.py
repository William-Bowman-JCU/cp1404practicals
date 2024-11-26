from unreliable_car import UnreliableCar

car = UnreliableCar('WRX', 100, 79.54)

for i in range(20):
    car.drive(5)
    print(car)