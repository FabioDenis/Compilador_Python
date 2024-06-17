# Importamos la clase lex del módulo ply, que utilizaremos para definir nuestro analizador léxico
import ply.lex as lex

# Definimos los tokens que serán reconocidos por nuestro analizador léxico
tokens = (
    'NUMBER',  # Token para representar números
    'PLUS',    # Token para representar el operador de suma
)

# Definimos la expresión regular para el token PLUS, que representa el operador de suma
t_PLUS = r'\+'

# Definimos los caracteres que serán ignorados por el analizador léxico (espacios y tabulaciones)
t_ignore = ' \t'

# Definimos una función para el token NUMBER, que convierte el valor del token a un entero
def t_NUMBER(t):
    r'\d+'       # Expresión regular para un número entero
    t.value = int(t.value)  # Convertimos el valor del token a entero
    return t

# Definimos una función para manejar errores léxicos, que imprime un mensaje y salta al siguiente token
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Creamos una instancia de la clase lex para nuestro analizador léxico
lexer = lex.lex()