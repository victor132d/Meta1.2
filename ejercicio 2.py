"""
Rosales Blanco Victor Ernesto
Creado: 23/02/2022
Ultima modificacion: 24/02/2022


Número perfecto. Diseñe una función
que encuentre el primer número
perfecto mayor que 28 (o un número
n dado). Un número es perfecto si
coincide con la suma de sus divisores
(excepto él mismo). Por ejemplo, 28 es
perfecto ya que 28 = 1 + 2 + 4 + 7 + 14.

Ejemplo:
perfecto(28)
496
perfecto(500)
8128


"""
p = float(input("Ingresa el peso del paciente: "))
h = float(input("Ingresa altura del paciente: "))

def calculaIMC():
    pass
    IMC= p/(h**2)
    return IMC

while calculaIMC() < 16:
    print("\n")
    print("El IMC del paciente es del "+ str(f"{calculaIMC():.2f}" + "%"))
    print("SALUDABLE")
    break

while 16 < calculaIMC() <= 17:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("INFRAPESO")
    break

while 17 < calculaIMC() <= 18:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("BAJO PESO")
    break

while 18 < calculaIMC() <= 25:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("SALUDABLE")
    break

while 25 < calculaIMC() <= 30:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("SOBREPESO")
    break

while 30 < calculaIMC() <= 35:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("SOBREPESO CRONICO")
    break

while 35 < calculaIMC() <= 40:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("OBESIDAD PREMORBIDA")
    break

while calculaIMC() > 40:
    print("\n")
    print("El IMC del paciente es del " + str(f"{calculaIMC():.2f}" + "%"))
    print("OBESIDAD MORBIDA")
    break


