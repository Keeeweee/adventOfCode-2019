from src import Parser
from src.Instructions import InputProvider
from itertools import permutations


def allParserHalted(parsers):
    for parser in parsers:
        if parser.state != Parser.Parser.STATE_HALT:
            return False
    return True


if __name__ == '__main__':
    with open('data/data.txt') as data:
        code = [int(x) for x in data.readline().split(',')]

    max = 0
    perm = []
    for permutation in permutations(range(5,10)):
        # print(permutation)
        codeCopy = code[:]
        parserA = Parser.Parser(code[:])
        parserB = Parser.Parser(code[:])
        parserC = Parser.Parser(code[:])
        parserD = Parser.Parser(code[:])
        parserE = Parser.Parser(code[:])

        parsers = (parserA, parserB, parserC, parserD, parserE)
        for index, parser in enumerate(parsers):
            parser.inputs.append(permutation[index])

        nextAmplifierValue = 0
        parserIndex = 0
        while not allParserHalted(parsers):
            parser = parsers[parserIndex % 5]
            # print(f'Using parser: {parserIndex % 5}')
            end = parser.run()
            while end == Parser.Parser.STATE_INPUT:
                parser.inputs.append(nextAmplifierValue)
                end = parser.run()

            nextAmplifierValue = parser.outputs[-1]
            # print(f'Next Amplifier Value: {nextAmplifierValue}')
            parserIndex += 1

        if nextAmplifierValue > max:
            max = nextAmplifierValue
            perm = permutation
    print(max)
