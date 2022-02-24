"""
Rosales Blanco Victor Ernesto
Creado: 23/02/2022
Ultima modificacion: 24/02/2022


Impuestos. Una empresa desea calcular
la estimación del importe de impuestos
que los empleados deben pagar. Los
ingresos inferiores a 8.000 euros no
están sujetos a impuestos; los comprendidos
entre 8.000 euros y 20.000 euros, lo están
al 18 %; los comprendidos entre 20.000
euros y 35.000 euros, están sujetos al 27%
y los superiores a 35.000 euros, lo están
al 38%. Diseña una función impuestos(x)
que calcule los impuestos correspondientes
a los ingresos x. Entrada: Un valor x de ingresos.

Salida: Los impuestos correspondientes a x con 2 decimales.


"""
sueldo = int(input("Escribe el sueldo del empleado: "))
impuesto = 0



def calculaImpuestos():
    pass
    impuestos= sueldo*impuesto
    return impuestos


if  sueldo <= 8000:
    print("\n")
    print("Sueldo bruto: " + str(sueldo))
    print("Impuesto: "+ str(impuesto))
    print("Sueldo neto: "+ str(sueldo))

else:
    if 8000 < sueldo <= 20000:
        impuesto = .18

        print("\n")
        print("Sueldo bruto: " + str(f"{sueldo:.2f}"))
        print("Impuesto: " + str(f"{calculaImpuestos():.2f}"))
        print("Sueldo Neto: " + str(f"{sueldo-calculaImpuestos():.2f}"))

    else:
        if 20000 < sueldo <= 35000:
            impuesto = .27

            print("\n")
            print("Sueldo bruto: " + str(f"{sueldo:.2f}"))
            print("Impuesto: " + str(f"{calculaImpuestos():.2f}"))
            print("Sueldo Neto: " + str(f"{sueldo - calculaImpuestos():.2f}"))

        else:
            if sueldo > 35000:
                impuesto = .38

                print("\n")
                print("Sueldo bruto: " + str(f"{sueldo:.2f}"))
                print("Impuesto: " + str(f"{calculaImpuestos():.2f}"))
                print("Sueldo Neto: " + str(f"{sueldo - calculaImpuestos():.2f}"))





