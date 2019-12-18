UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'

with open('data/data.txt') as data:
    cableOneDirections = data.readline().split(',')
    cableTwoDirections = data.readline().split(',')


def getCablePoints(directions):
    x = 0
    y = 0
    cable = []
    for segment in directions:
        steps = int(segment[1:])
        direction = segment[0]

        for step in range(steps):
            if direction == UP:
                y += 1
            if direction == DOWN:
                y -= 1
            if direction == LEFT:
                x -= 1
            if direction == RIGHT:
                x += 1
            cable.append((x, y))
    return cable


def stepsDistance(point, cableOne, cableTwo):
    return abs(cableOne.index(point)) + 1 + abs(cableTwo.index(point)) + 1


cableOne = getCablePoints(cableOneDirections)
cableTwo = getCablePoints(cableTwoDirections)

duplicatedTuples = list(set(cableOne).intersection(cableTwo))

min = stepsDistance(duplicatedTuples[0], cableOne, cableTwo)
for intersection in duplicatedTuples:
    candidate = stepsDistance(intersection, cableOne, cableTwo)
    if candidate < min:
        min = candidate

print(min)
