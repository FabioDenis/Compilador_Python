def semantic_analysis(ast):
    for node in ast.children:
        if node.type == 'ID' and node.value == 'imprimir':
            pass  # Example of semantic check
        elif node.type == 'NUMBER':
            pass  # Example of semantic check
        else:
            raise ValueError(f'Semantic error in node: {node}')