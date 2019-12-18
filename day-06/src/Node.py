class Node:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.visited = False

    def addChild(self, child: str):
        child = Node(child, self)
        self.children.append(child)
        return child

    def getDepth(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.getDepth()

    def getPath(self, target):
        self.visited = True
        if target == self:
            return [self]

        toVisit = self.children

        if self.parent is not None:
            toVisit.append(self.parent)

        success = None
        for visit in toVisit:
            if not visit.visited:
                success = visit.getPath(target)
                if success is not None:
                    success.append(self)
                    return success
        return success

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

