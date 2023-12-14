def leerURL (url):
    import urllib.request
    file = urllib.request.urlopen(url)
    texto = file.read()
    palabras = texto.split()
    numero = len(palabras)
    print (numero)



url = "http://textfiles.com/adventure/aencounter.txt"
leerURL (url)