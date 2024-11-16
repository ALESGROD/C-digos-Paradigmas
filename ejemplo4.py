try:
    archivito= open ("c:/Users/nurit/OneDrive/Documentos/PARADIGMAS DE PROGRAMACION/ejemplo2.py")
    data=archivito.read ()
    print(data)
except IOError: 
    print("Error al leer el archivo")
finally:
    archivito.close ()