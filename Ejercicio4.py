import urllib.request
url = "http://textfiles.com/adventure/aencounter.txt"
def leerURL (url):
    file = urllib.request.urlopen(url)
    texto = file.read()
    palabras = texto.split()
    numero = len(palabras)
    print (numero)

leerURL (url)