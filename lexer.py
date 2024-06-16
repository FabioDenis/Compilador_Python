import re

def tokenize(code):
    tokens = []
    token_specification = [
        ('NUMBER',   r'\d+'),       # Integer
        ('ID',       r'[A-Za-z]+'), # Identifiers
        ('OP',       r'[+\-*/]'),   # Arithmetic operators
        ('PRINT',    r'imprimir'),  # Print keyword
        ('WHITESPACE',  r'[ \t]+'), # Whitespace
        ('NEWLINE', r'\n'),         # Line endings
        ('MISMATCH', r'.'),         # Any other character
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'WHITESPACE' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected token: {value}')
        tokens.append((kind, value))
    return tokens