from src import Parser

if __name__ == '__main__':
    with open('data/data.txt') as data:
        code = [int(x) for x in data.readline().split(',')]

    parser = Parser.Parser(code)

    parser.run()

    print(parser.outputs[-1])