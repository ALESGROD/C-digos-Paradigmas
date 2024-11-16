class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        # Inicializa una nueva cuenta bancaria con el nombre del titular y un saldo inicial
        self.__titular = titular  # Guarda el nombre del titular de la cuenta como un atributo privado
        self.__saldo = saldo      # Guarda el saldo inicial de la cuenta como un atributo privado
        
    def depositar(self, cantidad):
        # Método para depositar una cantidad de dinero en la cuenta
        if cantidad > 0:  # Verifica si la cantidad a depositar es positiva
            self.__saldo += cantidad  # Agrega la cantidad al saldo actual
            print(f"Se han agregado ${cantidad} a tu cuenta. Saldo actual: ${self.__saldo}.")  # Informa al usuario sobre el depósito exitoso
        else:
            print("Operación no permitida: No se puede depositar una cantidad negativa.")  # Informa al usuario si el depósito es inválido
            
    def retirar(self, cantidad):
        # Método para retirar una cantidad de dinero de la cuenta
        if cantidad > self.__saldo:  # Verifica si la cantidad a retirar es mayor que el saldo disponible
            print("Fondos insuficientes: No puedes retirar más de lo que tienes.")  # Informa al usuario si intenta retirar más de lo que tiene
        elif cantidad <= 0:  # Verifica si la cantidad a retirar es negativa o cero
            print("Operación no permitida: La cantidad a retirar debe ser positiva.")  # Informa al usuario si la cantidad es inválida
        else:
            self.__saldo -= cantidad  # Resta la cantidad al saldo actual
            print(f"Has retirado ${cantidad}. Tu nuevo saldo es: ${self.__saldo}.")  # Informa al usuario sobre el retiro exitoso
            
    def consultar_saldo(self):
        # Método para consultar el saldo actual de la cuenta
        return self.__saldo  # Devuelve el saldo actual
    
    def consultar_titular(self):
        # Método para consultar el nombre del titular de la cuenta
        return self.__titular  # Devuelve el nombre del titular de la cuenta
    
# Imprimir una línea de separación para mayor claridad visual en la salida
print("="*66)

# Solicitar al usuario el nombre del titular de la cuenta
nombre_titular = input("Por favor, ingrese el nombre del titular de la cuenta: ")

# Solicitar al usuario el saldo inicial de la cuenta y convertirlo a número decimal
saldo_inicial = float(input("Por favor, ingrese el saldo inicial de la cuenta: "))

# Crear una instancia de CuentaBancaria utilizando el nombre del titular y el saldo inicial proporcionados
cuenta = CuentaBancaria(nombre_titular, saldo_inicial)

# Limpiar la pantalla para que la interfaz se vea más ordenada (solo en sistemas Windows)
import os  # Importar el módulo os para acceder a funciones del sistema operativo
os.system('cls')  # Ejecutar el comando 'cls' para limpiar la pantalla en Windows

# Imprimir una línea de separación para mayor claridad visual en la salida
print("="*66)

# Iniciar un bucle infinito para mostrar el menú de opciones al usuario
while True:
    # Mostrar las opciones disponibles para el usuario
    print("\nElige una de las siguientes opciones:")
    print("1. Agregar dinero")
    print("2. Extraer dinero")
    print("3. Verificar saldo")
    print("4. Verificar titular")
    print("5. Salir")
    
    # Solicitar al usuario que elija una opción del menú
    opcion = input("¿Cuál es tu elección?: ")
    
    # Ejecutar la acción correspondiente según la opción seleccionada por el usuario
    if opcion == "1":
        # Solicitar la cantidad de dinero que el usuario desea depositar
        cantidad = float(input("¿Cuánto dinero quieres depositar?: "))
        cuenta.depositar(cantidad)  # Llamar al método depositar con la cantidad ingresada
    elif opcion == "2":
        # Solicitar la cantidad de dinero que el usuario desea retirar
        cantidad = float(input("¿Cuánto dinero quieres retirar?: "))
        cuenta.retirar(cantidad)  # Llamar al método retirar con la cantidad ingresada
    elif opcion == "3":
        # Consultar y mostrar el saldo actual de la cuenta
        print(f"Tu saldo disponible es: ${cuenta.consultar_saldo()}")
    elif opcion == "4":
        # Consultar y mostrar el nombre del titular de la cuenta
        print(f"El titular registrado en la cuenta es: {cuenta.consultar_titular()}")
    elif opcion == "5":
        # Salir del sistema si el usuario elige la opción de salir
        print("Gracias por utilizar nuestros servicios bancarios. ¡Hasta la próxima!")
        break  # Romper el bucle y terminar el programa
    else:
        # Informar al usuario si selecciona una opción inválida
        print("Opción no válida. Por favor, selecciona una opción válida.")
