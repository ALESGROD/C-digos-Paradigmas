# Clase base (superclase)
class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def describir(self):
        return f"Vehículo {self.marca} del año {self.año}"

# Subclase que hereda de Vehiculo
class Coche(Vehiculo):
    def describir(self):
        return f"Coche {self.marca} del año {self.año}."

# Otra subclase que hereda de Vehiculo
class Camion(Vehiculo):
    def describir(self):
        return f"Camión {self.marca} del año {self.año}."

# Función que demuestra polimorfismo
def mostrar_descripcion(vehiculo):

    print(vehiculo.describir())

# Ejemplo de uso
coche = Coche("Ferrari", 2022)
camion = Camion("Maserati", 2019)

mostrar_descripcion(coche)  # Imprime: Coche Toyota del año 2022, hace ruido de motor.
mostrar_descripcion(camion)  # Imprime: Camión Volvo del año 2019, hace ruido de motor y bocina.
