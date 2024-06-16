def execute(ast):
    for node in ast.children:
        if node.type == 'NUMBER':
            print(node.value)
        elif node.type == 'PRINT':
            for child in node.children:
                if child.type == 'NUMBER':
                    print(child.value)
                elif child.type == 'ID':
                    print(child.value)
