try:
    x= int(input("Introduce un número : "))
    y=10/x
except ValueError:
    print("Debes introducir un número válido. ")
except ZeroDivisionError:
    print("No se puede dividir por cero. ")