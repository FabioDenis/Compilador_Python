from lexer import tokenize
from parser import parse
from semantic_analyzer import semantic_analysis
from interpreter import execute

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

if __name__ == '__main__':
    code = read_input('example.txt')
    print("Source code:\n", code)
    tokens = tokenize(code)
    print("Tokens:\n", tokens)
    ast = parse(tokens)
    print("AST:\n", ast)
    semantic_analysis(ast)
    execute(ast)