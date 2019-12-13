from typing import List


class Instruction:
    arity = None

    def __init__(self, args):
        if len(args) != self.arity:
            raise ValueError

    def run(self, code: List[int]) -> (int, int):
        pass

    @classmethod
    def getArity(cls) -> int:
        return cls.arity
