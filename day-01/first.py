def getFuel(mass):
    return int(mass / 3) - 2


masses = [int(line.rstrip('\n')) for line in open('data/data.txt')]

print(sum(map(getFuel, masses)))
