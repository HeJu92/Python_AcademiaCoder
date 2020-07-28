# En Python existen dos tipos de datos: numéricos y cadenas. También booleanos

# Numéricos:
    # Enteros (int):
entero = 10

    # Flotantes (float):
flotante = 10.05

    # Complejos (complex):
complejo = (10.05 + 0j) # No se explica

# Si, por ejemplo, usamos el comando "int(flotante)", solo nos mostrará la parte entera del número flotante

# Mediante el comando "type(variable)" podemos ver de que tipo es la variable

# Booleanos (bool)
# verdadero (true) y falso (false):
verdadero = True
falso = False

# Si usando la función "bool(algo)", algo es igual a 0, dará "False". En cualquier otro caso será "True".
# Funciona de la misma forma con cadenas de texto. Si la cadena de texto está vacía, será "False". En caso contrario será "True"

# Cadenas de texto (str)
cadena = "Hola mundo" # También sirven comillas simples

numero = str(entero) # Guarda número como cadena de texto y no como número entero.

# Uso de comillas dentro de comillas en cadena de texto. Y viceversa
comillas = "Esto tiene 'comillas simples' dentro de la cadena de texto"

# Escape de caracteres (\")
cadena2 = "Esto es una cadena\nEstoy en otra \"línea\""
