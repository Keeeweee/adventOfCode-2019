from math import atan2

ASTEROID = '#'
ROUND = 2


def getAngle(a, b):
    diff = (a[0] - b[0], a[1] - b[1])
    return atan2(diff[1], diff[0])


def getAsteroidsInsight(a, b, map) -> int:
    vectors = set()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ASTEROID and (x, y) != (a, b):
                vectors.add(getAngle((x, y), (a, b)))

    return len(vectors)


if __name__ == '__main__':
    map = [list(line.rstrip('\n')) for line in open('data/data.txt')]

    maxAsteroids = 0
    maxPosition = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ASTEROID:
                asteroidsInSight = getAsteroidsInsight(x, y, map)
                if maxAsteroids < asteroidsInSight:
                    maxAsteroids = asteroidsInSight
                    maxPosition = (x, y)

    print(maxAsteroids)
