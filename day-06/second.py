from src import Node


def createTree(orbits, root: Node, nodeList):
    if root.name in orbits:
        for child in orbits[root.name]:
            childNode = root.addChild(child)
            nodeList[childNode.name] = childNode
            createTree(orbits, childNode, nodeList)


mapRaw = [line.rstrip('\n').split(')') for line in open('data/data.txt')]

orbits = {}

for pair in mapRaw:
    if pair[0] not in orbits:
        orbits[pair[0]] = [pair[1]]
    else:
        orbits[pair[0]].append(pair[1])

rootNode = Node('COM', None)
nodeList = {'COM': rootNode}
createTree(orbits, rootNode, nodeList)

youNode = nodeList['YOU']
sanNode = nodeList['SAN']
path = youNode.getPath(sanNode)
print(len(path) - 3)  # Need to account for YOU, SAN and the fact you are already in orbit around somebody
