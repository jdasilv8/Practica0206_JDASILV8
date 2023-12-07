numero = (int(input("Introduce un número: ")))
def ficherotabla (n):
    tabla = []
    for i in range(0,11):
        valor = n * i
        file = open("Tabla del", 'w')
        file.write (n, "*" , i, "=", valor)
    return

ficherotabla (numero)