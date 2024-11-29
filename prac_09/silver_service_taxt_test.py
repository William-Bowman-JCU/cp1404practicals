from silver_service_taxi import SilverServiceTaxi

car = SilverServiceTaxi('Hummer', 200, 3)
print(car)
car.drive(20.5)
print(f'${car.get_fare():.2f}')
assert car.get_fare() == 80.1