from guitar import Guitar

gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
zeppeli = Guitar('Zeppeli M4', 2013, 10000.80)

print(gibson.get_age())
print(zeppeli.get_age())
print(gibson.is_vintage())
print(zeppeli.is_vintage())
