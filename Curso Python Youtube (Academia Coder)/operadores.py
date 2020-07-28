# Los operadores son signos, símbolos o palabras que el intérprete utiliza para hacer una operación específica

# Operadores matemáticos

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5

    # Operador de suma (+)
suma = numero1 + numero2
#print(suma)
    # Operador de resta (-)
resta = numero1 - numero2
#print(resta)
    # Operador de negativo (-)
negativo = -10 + numero2
#print(negativo)
negativo2 = numero2 - numero1
#print(negativo2)
    # Operador de multiplicación (*)
multiplicacion = numero1 * numero2
#print(multiplicacion)
    # Operador de exponente (**)
exponente = numero1 ** numero2
#print(exponente)
    # Operador de división (/)
division = numero1 / numero2
#print(division)
    # Operador de división entera (//)
division2 = numero1 // numero2
#print(division2)
    # Operador de módulo o resto (%)
resto = numero1 % numero2
#print(resto)

# Comentario de varias líneas (""")
"""
El orden de precedencia para las operaciones es:
1. Paréntesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Resta
"""

# Reglas de precedencia
resultado = 12 * 5 + 2 / 3 ** 2
#print(resultado)
resultado2 = (12 * 5) + (2 / 3) ** 2
#print(resultado2)

# Operadores para cadenas de texto
cadena1 = "Hola "
cadena2 = "Mundo"

    # Operadores de concatenación
cadenas = cadena1 + cadena2
#print(cadenas)

    # Operadores de repetición
cadenas_repetidas = cadena1 * 3
#print(cadenas_repetidas)

# Operadores de relación
# Estos operadores evaluan si 2 o más objetos cumplen una condición
# El resultado de dicha evaluación es un objeto booleano (bool)
"""
== Igual a
!= Distinto de
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
"""

igual = numero1 == numero2
#print(igual)
distinto = numero1 != numero2
#print(distinto)
mayor_que = numero1 > numero2
#print(mayor_que)
menor_que = numero2 < numero1
#print(menor_que)
mayor_igual = numero1 >= numero5

# Operadores de asignación
    # Asignación simple (=)
a1, a2, a3, a4, a5 = 1, 2, 3, 4, 5 # Es igual a "a1 = 1" y "a2 = 2..."
    # Asignación suma (+=)
a1 = a1 + a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 += a2
#print(a1)
    # Asignación resta (-=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 - a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 -= a2
#print(a1)
    # Asignación multiplicación (*=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 * a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 *= a2
#print(a1)
    # Asignación exponente (**=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 ** a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 **= a2
#print(a1)
    # Asignación división(/=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 / a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 /= a2
#print(a1)
    # Asignación división entera (//=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 // a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 //= a2
#print(a1)
    # Asignación división ¿? (%=)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 = a1 % a2
#print(a1)
a1 = 1 #Para que el valor de a1 se mantenga como en la asignación
a1 %= a2
#print(a1)
