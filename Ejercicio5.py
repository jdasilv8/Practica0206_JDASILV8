ppais = input("Indica el pais: ")
file = open ('sdg_08_10.tsv', 'r')
texto = file.read()
lineas = texto.split("\n")
for i in range (1, len(lineas)):
    pais = lineas[i]
    pais = pais.split(",")
    linea = pais[2]
    contlinea = linea.split()
    if ppais.upper() == contlinea[0]:
        print (contlinea)