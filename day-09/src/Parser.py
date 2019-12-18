from .Instructions import Sum, Mult, Input, Output, Instruction, Equals, JumpIfFalse, JumpIfTrue, LessThan, \
    RelativeOffset
from typing import Dict


class Parser:
    STATE_START = 'START'
    STATE_RUN = 'RUN'
    STATE_INPUT = 'INPUT'
    STATE_OUTPUT = 'OUTPUT'
    STATE_HALT = 'HALT'

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
    REL_OPCODE = 9

    POS_MODE = 0
    INM_MODE = 1
    REL_MODE = 2

    def __init__(self, code):
        self.code = code
        self.pointer = 0
        self.outputs = []
        self.inputs = []
        self.state = self.STATE_START
        self.relModePos = 0

    def parseInstruction(self, code: Dict[int, int], pointer: int):
        instructionStr = str(code[pointer])
        # print(f'Instruction: {instructionStr}')
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
        if instruction not in [Output, JumpIfTrue, JumpIfFalse, RelativeOffset]:  # Add all instructions that DO NOT WRITE to the code
            if modes[-1] != self.REL_MODE:
                modes[-1] = self.INM_MODE

        args = []
        for i in range(arity):
            if instruction in [Input, Equals, Sum, Mult, LessThan] and i == arity - 1: # All of this is because writes are treated a bit diffenrent -.-
                args.append(self.getInputValueInPositionForMode(pointer + i + 1, modes[i]))
            else:
                args.append(self.getValueInPositionForMode(pointer + i + 1, modes[i]))

        if instruction == Input:
            newInput = self.inputs[0]
            self.inputs = self.inputs[1:]
            return instruction(args, newInput)

        return instruction(args)

    def getValueInPositionForMode(self, position, mode):
        if mode == self.POS_MODE:
            return self.getValueInPosition(self.getValueInPosition(position))
        elif mode == self.INM_MODE:
            return self.getValueInPosition(position)
        elif mode == self.REL_MODE:
            return self.getValueInPosition(self.relModePos + self.getValueInPosition(position))
        else:
            raise ValueError

    def getInputValueInPositionForMode(self, position, mode):
        if mode == self.POS_MODE:
            return self.getValueInPosition(self.getValueInPosition(position))
        elif mode == self.INM_MODE:
            return self.getValueInPosition(position)
        elif mode == self.REL_MODE:
            return self.relModePos + self.getValueInPosition(position)
        else:
            raise ValueError

    def getValueInPosition(self, position):
        if position in self.code:
            return self.code[position]
        else:
            self.code[position] = 0
            return 0

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
        if instruction == self.REL_OPCODE:
            return RelativeOffset
        else:
            raise ValueError

    def run(self):
        self.state = self.STATE_RUN
        while self.code[self.pointer] != self.HALT_OPCODE:
            # print('--------------------------------')
            # print(f'RelOffset: {self.relModePos}')
            if self.code[self.pointer] == self.INPUT_OPCODE and len(self.inputs) == 0:
                self.state = self.STATE_INPUT
                return self.STATE_INPUT
            instruction = self.parseInstruction(self.code, self.pointer)
            # print(str(instruction))
            output, self.pointer = instruction.run(self.code, self.pointer)
            # print(f'Pointer: {self.pointer}')

            if type(instruction) is RelativeOffset:
                self.relModePos += output

            if type(instruction) is Output:
                self.outputs.append(output)
                self.state = self.STATE_OUTPUT
                return self.STATE_OUTPUT
        # print(self.outputs)
        # print(self.code)
        self.state = self.STATE_HALT
        return self.STATE_HALT
