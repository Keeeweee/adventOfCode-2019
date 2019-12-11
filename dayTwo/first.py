MIN_CODE_LENGTH = 3

HALT_INSTRUCTION = 99
SUM_INSTRUCTION = 1
MULT_INSTRUCTION = 2

with open('data/first.txt') as data:
    code = [int(x) for x in data.readline().split(',')]

if len(code) < MIN_CODE_LENGTH:
    print(f'Code should have length bigger than {MIN_CODE_LENGTH}. Found {len(code)}.')
    raise ValueError

code[1] = 12
code[2] = 2

for index in range(0, len(code), 4):
    instruction = code[index]
    if instruction == HALT_INSTRUCTION:
        break

    if index + 3 >= len(code):
        print('This code is not valid.')
        raise ValueError

    if instruction == SUM_INSTRUCTION:
        code[code[index + 3]] = code[code[index + 1]] + code[code[index + 2]]

    if instruction == MULT_INSTRUCTION:
        code[code[index + 3]] = code[code[index + 1]] * code[code[index + 2]]


print(code[0])
