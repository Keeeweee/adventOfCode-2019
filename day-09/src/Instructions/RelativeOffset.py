from .Instruction import Instruction


class RelativeOffset(Instruction):
    arity = 1

    def __init__(self, args):
        super().__init__(args)
        self.relOffset = args[0]

    def run(self, code, pointer):
        return self.relOffset, pointer + self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[REL] Modify offset {self.relOffset}'
