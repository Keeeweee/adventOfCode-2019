from .Instruction import Instruction


class JumpIfFalse(Instruction):
    arity = 2

    def __init__(self, args):
        super().__init__(args)
        self.condition = args[0]
        self.jump = args[1]

    def run(self, code, pointer):
        if self.condition == 0:
            return None, self.jump
        return None, pointer + self.arity + 1

    @classmethod
    def getArity(cls):
        return cls.arity

    def __str__(self):
        return f'[JiF] If {self.condition} == 0 => pointer = {self.jump}'
