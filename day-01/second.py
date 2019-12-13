def getFuel(mass):
    newMass = int(mass / 3) - 2
    if newMass <= 0:
        return 0
    return newMass + getFuel(newMass)


masses = [int(line.rstrip('\n')) for line in open('data/data.txt')]

print(sum(map(getFuel, masses)))
