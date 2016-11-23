##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##ALGORITMOS FUNDAMENTALES
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: PRACTICA DE MANEJO DE ARCHIVOS

print("\t\t\t     Escuela Politécnica Nacional")
print("\t\t\t  Escuela de Formación de Tecnólogos")
print("\t\t\t\t  Programación Avanzada")
print("\t\t\t     Diana Bonilla - Valeria Ochoa")

nuevo = open ('Resultado.txt','a')
arch=open('Amistad.txt','r')
def leertxt():
    
    total=0
    linea=arch.readline()
    while linea !="":
        print (linea)
        linea=arch.readline()
        total=len(linea)+total
        print (total)
    arch.close()
    nuevo.write("Nuevo archivo: "+str(total))

    nuevo.close()
leertxt()




