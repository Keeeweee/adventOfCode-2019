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


def manhatanDistance(point):
    return abs(point[0]) + abs(point[1])


def getIntersections(cableOne, cableTwo):
    intersections = []
    for segment in cableOne:
        if segment in cableTwo:
            intersections.append(segment)
            print(segment)
    return intersections


cableOne = getCablePoints(cableOneDirections)
cableTwo = getCablePoints(cableTwoDirections)

duplicatedTuples = list(set(cableOne).intersection(cableTwo))

min = manhatanDistance(duplicatedTuples[0])
for intersection in duplicatedTuples:
    candidate = manhatanDistance(intersection)
    if candidate < min:
        min = candidate

print(min)
