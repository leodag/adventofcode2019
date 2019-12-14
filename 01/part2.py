import sys

def fuel_needed(weight):
    "finds the fuel needed for a given weight"
    return max(weight // 3 - 2, 0)

def total_fuel(module_weight):
    "finds the total fuel needed for a module and it's fuel"
    total_fuel = 0

    addfuel = fuel_needed(module_weight)
    while addfuel > 0:
        total_fuel += addfuel
        addfuel = fuel_needed(addfuel)

    return total_fuel

if __name__ == '__main__':
    fuel = 0

    for module_weight in sys.stdin.readlines():
        fuel += total_fuel(int(module_weight))

    print(fuel)
