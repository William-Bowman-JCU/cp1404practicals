from unreliable_car import UnreliableCar

car = UnreliableCar('WRX', 100, 2.54)

for i in range(100):
    car.drive(15)
    print(car)