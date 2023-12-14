file = open ('sdg_08_10.tsv', 'r')
texto = file.read()
texto = str(texto)
lineas = texto.split("\n")
print (lineas[1])
for i in lineas:
    pais = lineas[i+1]