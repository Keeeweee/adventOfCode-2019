from src import Parser

if __name__ == '__main__':
    with open('data/data.txt') as data:
        code = {i: int(x) for i, x in enumerate(data.readline().split(','))}

    parser = Parser.Parser(code)
    parser.inputs.append(2)
    end = parser.run()
    while end != Parser.Parser.STATE_HALT:
        if end == Parser.Parser.STATE_INPUT and parser.inputs != 0:
            parser.inputs.append(input("Input: "))
        end = parser.run()
    print(parser.outputs)
