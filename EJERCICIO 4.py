"""
Rosales Blanco Victor Ernesto
Creado: 23/02/2022
Ultima modificacion: 24/02/2022


Triángulo de asteriscos. Escribir
una función no productiva triang(n)
que, dado un número n, imprime un
"triángulo de asteriscos de tamaño n".

"""

def triangulo():
    return "\n".join([" "*(filas-espacios)+"*"*(espacios+espacios-1) for espacios in range(1,filas+1)])

filas = int(input("Ingresa numero de filas: "))
print(triangulo())

