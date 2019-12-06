def calculate_fuel(mass):
    fuel = 0
    new_mass = mass
    while True:
        new_mass = new_mass / 3 - 2
        if new_mass > 0:
            fuel += new_mass
        else:
            return fuel


with open('input.txt') as f:
    print(sum([calculate_fuel(int(x))for x in f]))
