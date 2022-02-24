"""
Rosales Blanco Victor Ernesto
Creado: 23/02/2022
Ultima modificacion: 24/02/2022


IMC. Diseña una función imc(p,h) que
reciba reciba el peso p y la altura h
de una persona, calcule el índice de
masa corporal de una persona (IMC =
peso[kg]/altura²[m]) y retorne el estado
en el que se encuentra esa persona en
función del valor de IMC:

"""

def numPerfecto():
    contador = 0
    divisorP = 0

    for divisor in range(1, numero):
        if (numero % divisor) == 0:
            print(divisor)
            contador += 1
            divisorP = divisorP + divisor

    print("\n")
    print("El numero " + str(numero) + " tiene " + str(contador) + " divisores")
    print("La suma de los divisores es de " + str(divisorP))

    if divisorP == numero:
        return print("***EL NUMERO ES PERFECTO***")
    else:
        return print("***EL NUMERO NO ES PERFECTO***")



numero = int(input("Introduzca el numero:"))
numPerfecto()


