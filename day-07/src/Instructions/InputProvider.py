class InputProvider:
    def __init__(self, preDefinedInput, amplifierInput):
        self.preDefinedInput = preDefinedInput
        self.amplifierInput = amplifierInput
        self.parity = 0

    def getNextValue(self):
        if self.parity % 2 == 0:
            self.parity += 1
            # print(f'Providing input: {self.preDefinedInput}')
            return self.preDefinedInput
        else:
            self.parity += 1
            # print(f'Providing input: {self.amplifierInput}')
            return self.amplifierInput