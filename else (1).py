try:
    x= int (input ("Introduce un numero: "))
except ValueError:
    print ("Debes introducir un número valido. ")
else: 
    print (f"El numero es {x}")