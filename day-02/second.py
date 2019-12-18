MIN_CODE_LENGTH = 3

HALT_INSTRUCTION = 99
SUM_INSTRUCTION = 1
MULT_INSTRUCTION = 2

DESIRED_OUTPUT = 19690720

with open('data/data.txt') as data:
    code = [int(x) for x in data.readline().split(',')]

if len(code) < MIN_CODE_LENGTH:
    print(f'Code should have length bigger than {MIN_CODE_LENGTH}. Found {len(code)}.')
    raise ValueError


def calculateState(code, noun, verb):
    state = code[:]
    state[1] = noun
    state[2] = verb

    for index in range(0, len(state), 4):
        instruction = state[index]
        if instruction == HALT_INSTRUCTION:
            break

        if index + 3 >= len(state):
            print('This code is not valid.')
            raise ValueError

        if instruction == SUM_INSTRUCTION:
            state[state[index + 3]] = state[state[index + 1]] + state[state[index + 2]]

        if instruction == MULT_INSTRUCTION:
            state[state[index + 3]] = state[state[index + 1]] * state[state[index + 2]]

    return state[0]


for noun in range(0, 100):
    for verb in range(0, 100):
        if calculateState(code, noun, verb) == DESIRED_OUTPUT:
            print(noun * 100 + verb)
