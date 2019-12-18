from src import Node
import functools

def createTree(orbits, root: Node, nodeList):
    if root.name in orbits:
        for child in orbits[root.name]:
            childNode = root.addChild(child)
            nodeList.append(childNode)
            createTree(orbits, childNode, nodeList)


mapRaw = [line.rstrip('\n').split(')') for line in open('data/data.txt')]

orbits = {}

for pair in mapRaw:
    if pair[0] not in orbits:
        orbits[pair[0]] = [pair[1]]
    else:
        orbits[pair[0]].append(pair[1])

rootNode = Node('COM', None)
nodeList = [rootNode]
createTree(orbits, rootNode, nodeList)

count = 0
for node in nodeList:
    count += node.getDepth()
print(count)
