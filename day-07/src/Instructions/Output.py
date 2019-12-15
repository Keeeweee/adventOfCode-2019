from .Instruction import Instruction


class Output(Instruction):
    arity = 1

    def __init__(self, args):
        super().__init__(args)
        self.read = args[0]

    def run(self, code, pointer):
        return self.read, pointer + self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[OUT] {self.read}'
