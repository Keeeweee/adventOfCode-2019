from math import atan2, pi

ASTEROID = '#'
ROUND = 2


def getAngle(a, b):
    diff = (a[0] - b[0], a[1] - b[1])
    return -atan2(diff[1], diff[0]) * 180 / pi


def getAsteroidsInsight(a, b, map) -> int:
    vectors = set()
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ASTEROID and (x, y) != (a, b):
                vectors.add(getAngle((x, y), (a, b)))

    return len(vectors)


def getAsteroidsMap(basePosition, map):
    asteroidMap = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ASTEROID and (x, y) != basePosition:
                angle = getAngle((x, y), basePosition)
                if angle not in asteroidMap:
                    asteroidMap[angle] = [(x, y)]
                else:
                    asteroidMap[angle].append((x, y))
    for angle in asteroidMap:
        asteroidMap[angle] = sorted(asteroidMap[angle],
            key=lambda p: ((p[0] - basePosition[0]) ** 2 + (p[1] - basePosition[1]) ** 2))
    return asteroidMap


if __name__ == '__main__':
    map = [list(line.rstrip('\n')) for line in open('data/test_05.txt')]

    maxAsteroids = 0
    maxPosition = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ASTEROID:
                asteroidsInSight = getAsteroidsInsight(x, y, map)
                if maxAsteroids < asteroidsInSight:
                    maxAsteroids = asteroidsInSight
                    maxPosition = (x, y)

    basePosition = maxPosition
    asteroidsMap = getAsteroidsMap(basePosition, map)
    sortedAngleMap = []
    count = 0
    for key in sorted(asteroidsMap.keys(), key= lambda k: k if k >= -90 else k + 360, reverse=True):
        sortedAngleMap.append({'angle': key, 'asteroids': asteroidsMap[key], 'index': count})
        count += 1
    print(maxPosition)
    print(maxAsteroids)
    print(atan2(1, 0) * 180 / pi)
    print(sortedAngleMap)

    print(sortedAngleMap[200]['asteroids'][0][0]*100 + sortedAngleMap[200]['asteroids'][0][1])
