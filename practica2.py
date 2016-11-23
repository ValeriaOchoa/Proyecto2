##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##ALGORITMOS FUNDAMENTALES
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: PRACTICA DE MANEJO DE ARCHIVOS

def creartxt():
    archi=open('datos.txt','w')
    archi.close()
def grabartxt():
    archi = open('datos.txt','a')
    archi.write('Diana Bonilla\n')
    archi.write('Valeria Ochoa\n')
    archi.close()
creartxt()
grabartxt()
