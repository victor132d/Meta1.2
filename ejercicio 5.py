"""
Rosales Blanco Victor Ernesto
Creado: 23/02/2022
Ultima modificacion: 24/02/2022


Es primo?. Diseña una función
es_primo(n) que reciba un natural
n y devuelva True si el número es
primo o False en caso contrario.
Se asume que n > 1.

"""


def numPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    else:
        print("Es primo")
        return True

num= int(input("Introduce un numero: "))
numPrimo(num)