numero = (int(input("Introduce un número: ")))
def ficherotabla (n):
    file = open("tabla-" + str(n) + ".txt",'w')
    for i in range(1,11):
        valor = n * i
        file.write (str(n) + "*" + str(i) + "=" + str(valor) + "\n")
    return

ficherotabla (numero)