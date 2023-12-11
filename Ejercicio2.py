numero = (int(input("Introduce un número del 1 al 10: ")))
def leertabla (n):
    file = open("tabla-" + str(n) + ".txt", 'r')
    print (file.read())