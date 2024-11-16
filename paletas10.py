from abc import ABC, abstractmethod

# Excepción personalizada
class PrecioInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Interfaz de la paleta
class Paleta(ABC):
    def __init__(self, sabor, precio):
        self.sabor = sabor
        if precio < 0:
            raise PrecioInvalidoError("El precio no puede ser negativo.")
        self.precio = precio

    @abstractmethod
    def mostrarInformacion(self):
        pass

    @abstractmethod
    def cambiarPrecio(self):
        pass

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, baseAgua):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua

    def mostrarInformacion(self):
        print(f"Sabor: {self.sabor}, Precio: {self.precio} pesos")
        print(f"Base de agua: {'Sí' if self.baseAgua else 'No'}")

    def cambiarPrecio(self):
        try:
            if self.precio < 0:
                raise PrecioInvalidoError("El precio no puede ser negativo.")
            self.precio += 2
        except PrecioInvalidoError as e:
            print(f"Error al cambiar el precio: {e}")

class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrarInformacion(self):
        print(f"Sabor: {self.sabor}, Precio: {self.precio} pesos")
        print(f"Textura cremosa: {'Sí' if self.cremosa else 'No'}")

    def cambiarPrecio(self):
        try:
            if self.precio < 0:
                raise PrecioInvalidoError("El precio no puede ser negativo.")
            self.precio += 6
        except PrecioInvalidoError as e:
            print(f"Error al cambiar el precio: {e}")

def imprimir_informacion_paleta(paleta):
    paleta.mostrarInformacion()
    paleta.cambiarPrecio()
    paleta.mostrarInformacion()

# Instancias de PaletaAgua y PaletaCrema
try:
    paleta1 = PaletaAgua("Fresa", 10, True)
    paleta2 = PaletaCrema("Chocolate", 12, True)
    imprimir_informacion_paleta(paleta1)
    imprimir_informacion_paleta(paleta2)
except PrecioInvalidoError as e:
    print(f"Excepción: {e}")
