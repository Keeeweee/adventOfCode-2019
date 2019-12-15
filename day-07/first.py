from src import Parser
from src.Instructions import InputProvider
from itertools import permutations

if __name__ == '__main__':
    with open('data/data.txt') as data:
        code = [int(x) for x in data.readline().split(',')]

    max = 0
    perm = []
    for permutation in permutations(range(5)):
        # print(permutation)
        codeCopy = code[:]
        amplifierValue = 0
        for num in permutation:
            inputProvider = InputProvider(num, amplifierValue)
            parser = Parser.Parser(code, inputProvider)
            parser.run()
            amplifierValue = parser.outputs[-1]
        if amplifierValue > max:
            max = amplifierValue
            perm = permutation
    print(max)