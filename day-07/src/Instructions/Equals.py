from .Instruction import Instruction


class Equals(Instruction):
    arity = 3

    def __init__(self, args):
        super().__init__(args)
        self.first = args[0]
        self.second = args[1]
        self.write = args[2]

    def run(self, code, pointer):
        code[self.write] = int(self.first == self.second)
        return None, pointer + self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[EQ] Write {self.first} == {self.second} at {self.write} => {int(self.first == self.second)} -> {self.write}'
