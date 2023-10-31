# Ejemplo de funciones de orden superior en Python

# Función de orden superior que toma una función como argumento
def apply_function(func, value):
    return func(value)

# Función lambda que eleva al cuadrado un número
square = lambda x: x ** 2

# Función lambda que verifica si un número es par
is_even = lambda x: x % 2 == 0

# Función lambda que suma dos números
add = lambda x, y: x + y

# Ejemplo de aplicación de funciones de orden superior
number = 5

# Aplicar la función square para elevar al cuadrado
result_square = apply_function(square, number)
print(f"{number} elevado al cuadrado es {result_square}")

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar map para aplicar la función square a todos los elementos de la lista
squared_numbers = list(map(square, numbers))
print("Números elevados al cuadrado:", squared_numbers)

# Usar filter para obtener los números pares de la lista
even_numbers = list(filter(is_even, numbers))
print("Números pares:", even_numbers)

# Usar reduce para sumar todos los elementos de la lista
from functools import reduce
total_sum = reduce(add, numbers)
print("Suma de todos los números:", total_sum)
