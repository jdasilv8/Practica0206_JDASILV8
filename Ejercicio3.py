import os
numero = (int(input("Introduce un número del 1 al 10: ")))
line = (int(input("Introduce otro número del 1 al 10: ")))
def leertabla (n, lin):
    existe = os.path.isfile ("tabla-" + str(n) + ".txt")
    if existe == True:
        file = open("tabla-" + str(n) + ".txt", 'r')
        linea = file.readlines()
        print (linea[lin - 1])
    else:
        print ("El archivo con el nombre tabla", n ,"no existe")

leertabla (numero,line)