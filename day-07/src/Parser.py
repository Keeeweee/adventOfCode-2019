from .Instructions import Sum, Mult, Input, Output, Instruction, Equals, JumpIfFalse, JumpIfTrue, LessThan
from typing import List


class Parser:
    INSTRUCTION_LEN = 2

    HALT_OPCODE = 99
    SUM_OPCODE = 1
    MULT_OPCODE = 2
    INPUT_OPCODE = 3
    OUTPUT_OPCODE = 4
    JIT_OPCODE = 5
    JIF_OPCODE = 6
    LT_OPCODE = 7
    EQ_OPCODE = 8


    POS_MODE = 0
    INM_MODE = 1

    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.outputs = []

    def parseInstruction(self, code: List[int], pointer: int):
        instructionStr = str(code[pointer])
        if len(instructionStr) >= self.INSTRUCTION_LEN:
            instruction = self.getInstruction(int(instructionStr[-self.INSTRUCTION_LEN:]))
            modesStr = instructionStr[:-self.INSTRUCTION_LEN]
        else:
            instruction = self.getInstruction(int(instructionStr))
            modesStr = ''

        arity = instruction.getArity()

        modes = [int(x) for x in modesStr[::-1]]
        missingModesLen = arity - len(modes)

        for i in range(missingModesLen):
            modes.append(self.POS_MODE)
        if instruction not in [Output, JumpIfTrue, JumpIfFalse]: #Add all instructions that DO NOT WRITE
            modes[-1] = self.INM_MODE

        args = []
        for i in range(arity):
            if modes[i] == self.POS_MODE:
                args.append(code[code[pointer + i + 1]])
            elif modes[i] == self.INM_MODE:
                args.append(code[pointer + i +1])
            else:
                raise ValueError

        return instruction(args)

    def getInstruction(self, instruction) -> Instruction:
        if instruction == self.SUM_OPCODE:
            return Sum
        if instruction == self.MULT_OPCODE:
            return Mult
        if instruction == self.INPUT_OPCODE:
            return Input
        if instruction == self.OUTPUT_OPCODE:
            return Output
        if instruction == self.JIT_OPCODE:
            return JumpIfTrue
        if instruction == self.JIF_OPCODE:
            return JumpIfFalse
        if instruction == self.LT_OPCODE:
            return LessThan
        if instruction == self.EQ_OPCODE:
            return Equals
        else:
            raise ValueError

    def run(self):
        while self.code[self.pointer] != self.HALT_OPCODE:
            instruction = self.parseInstruction(self.code, self.pointer)
            # print(str(instruction))
            output, self.pointer = instruction.run(self.code, self.pointer)
            # print(f'Pointer: {self.pointer}')

            if output is not None:
                self.outputs.append(output)


        # print(self.outputs)
        # print(self.code)