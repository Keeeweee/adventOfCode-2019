from .Instruction import Instruction


class Mult(Instruction):
    arity = 3

    def __init__(self, args):
        super().__init__(args)
        self.first = args[0]
        self.second = args[1]
        self.write = args[2]

    def run(self, code):
        code[self.write] = self.first * self.second
        return None, self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[MULT] {self.first} * {self.second} = {self.first * self.second} -> {self.write}'
