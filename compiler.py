# Importamos el objeto parser del módulo parser, que contiene nuestro analizador sintáctico
from parser import yacc_parser

# Importamos las funciones necesarias del módulo codegen para generar código intermedio, optimizarlo y generar código final
from codegen import generate_intermediate_code, optimize_intermediate_code, generate_final_code

# Definimos una función para compilar código. La función toma una cadena de código como entrada y devuelve el código final compilado.
def compile_code(code):
    # Parseamos la cadena de código usando nuestro analizador sintáctico y obtenemos un árbol de análisis sintáctico
    parse_tree = yacc_parser.parse(code)
    # Generamos código intermedio a partir del árbol de análisis sintáctico
    intermediate_code = generate_intermediate_code(parse_tree)
    # Optimizamos el código intermedio
    optimized_code = optimize_intermediate_code(intermediate_code)
    # Generamos el código final a partir del código optimizado
    final_code = generate_final_code(optimized_code)
    # Devolvemos el código final compilado
    return final_code

# Esta condición se cumple si ejecutamos el script como programa principal
if __name__ == "__main__":
    # Solicitamos al usuario que ingrese una expresión para compilar
    code = input("Enter an expression to compile: ")
    # Compilamos la expresión ingresada por el usuario
    compiled_code = compile_code(code)
    # Imprimimos el código compilado
    print("Compiled code:", compiled_code)