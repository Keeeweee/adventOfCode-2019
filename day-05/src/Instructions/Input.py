from .Instruction import Instruction


class Input(Instruction):
    arity = 1

    def __init__(self, args):
        super().__init__(args)
        self.value = int(input("Input value: "))
        self.write = args[0]

    def run(self, code):
        code[self.write] = self.value
        return None, self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[INP] {self.value} -> {self.write}'
