import sys

def fuel_needed(weight):
    return max(weight // 3 - 2, 0)

fuel = 0

for line in sys.stdin.readlines():
    fuel += fuel_needed(int(line))

print(fuel)
