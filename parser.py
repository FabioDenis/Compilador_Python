class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

def parse(tokens):
    def parse_expression(index):
        token = tokens[index]
        if token[0] == 'NUMBER':
            return ASTNode('NUMBER', token[1]), index + 1
        elif token[0] == 'ID':
            return ASTNode('ID', token[1]), index + 1
        elif token[0] == 'PRINT':
            print_node = ASTNode('PRINT')
            next_node, new_index = parse_expression(index + 1)
            print_node.children.append(next_node)
            return print_node, new_index
        else:
            raise SyntaxError(f'Unexpected token: {token}')
    
    index = 0
    ast = ASTNode('ROOT')
    while index < len(tokens):
        node, index = parse_expression(index)
        ast.children.append(node)
    return ast