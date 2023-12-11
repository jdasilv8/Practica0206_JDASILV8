import os
numero = (int(input("Introduce un número del 1 al 10: ")))
def leertabla (n):
    existe = os.path.isfile ("tabla-" + str(n) + ".txt")
    if existe == True:
        file = open("tabla-" + str(n) + ".txt", 'r')
        print (file.read())
    else:
        print ("El archivo con el nombre tabla", n ,"no existe")

leertabla (numero)