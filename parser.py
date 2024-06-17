# Importamos la clase yacc del módulo ply, que utilizaremos para definir nuestro analizador sintáctico
import ply.yacc as yacc

# Importamos los tokens definidos en el analizador léxico
from lexer import tokens

# Definimos las reglas gramaticales para nuestro analizador sintáctico

# Regla para una expresión que consiste en una expresión seguida de un operador PLUS y un término
def p_expression_plus(p):
    'expression : expression PLUS term'
    # El valor de la expresión es la suma del valor de la expresión y el valor del término
    p[0] = p[1] + p[3]

# Regla para una expresión que consiste únicamente en un término
def p_expression_term(p):
    'expression : term'
    # El valor de la expresión es el valor del término
    p[0] = p[1]

# Regla para un término que consiste en un número
def p_term_number(p):
    'term : NUMBER'
    # El valor del término es el número encontrado
    p[0] = p[1]

# Función para manejar errores sintácticos
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Creamos una instancia de la clase yacc para nuestro analizador sintáctico
parser = yacc.yacc()
