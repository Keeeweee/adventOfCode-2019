from math import atan2, pi

ASTEROID = '#'
ROUND = 2


def getAngle(a, b):
    diff = (a[0] - b[0], a[1] - b[1])
    angle = atan2(diff[1], diff[0])
    if angle < 0:
        angle += 2 * pi
    angle = angle * 180 / pi
    angle += 90
    angle %= 360
    return angle


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

    basePosition = maxPosition
    asteroidsMap = getAsteroidsMap(basePosition, map)
    sortedAngleMap = []
    count = 0
    for key in sorted(asteroidsMap.keys()):
        sortedAngleMap.append({'angle': key, 'asteroids': asteroidsMap[key], 'index': count})
        count += 1

    print(sortedAngleMap[200 - 1]['asteroids'][0][0]*100 + sortedAngleMap[200-1]['asteroids'][0][1])
