##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##ALGORITMOS FUNDAMENTALES
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: PRACTICA DE MANEJO DE ARCHIVOS

import math
archi=open('funcion.txt','a')
print("\t\t\t     Escuela Politécnica Nacional")
print("\t\t\t  Escuela de Formación de Tecnólogos")
print("\t\t\t\t  Programación Avanzada")
print("\t\t\t     Diana Bonilla - Valeria Ochoa")
print("Ingrese los datos: ")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

raiz = b * b - 4 *a*c

if raiz < 0:
    print("Ingrese otros valores, la raiz es imaginaria: ", raiz)
    archi.write("La raiz es imaginaria\n")
else:
    x1=(-b+(math.sqrt(raiz)))/(2*a)
    x2=(-b-(math.sqrt(raiz)))/(2*a)
    print("x1= ",str(x1),"x2= ",str(x2))
    archi.write("X1= "+str(x1)+'\n')
    archi.write("X2= "+str(x2)+'\n')
archi.close()

