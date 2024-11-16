class Paleta:
    def _init_(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

    def mostrarInformacion(self):
        print(f"Sabor: {self.sabor}, Precio: {self.precio} pesos")
        
class PaletaAgua(Paleta):
    def _init_(self, sabor, precio, baseAgua):
        super()._init_(sabor, precio)
        self.baseAgua = baseAgua

    def mostrarBaseAgua(self):
        print(f"Base de agua: {'Sí' if self.baseAgua else 'No'}")

    def cambiarPrecio(self):
        self.precio += 2

class PaletaCrema(Paleta):
    def _init_(self, sabor, precio, cremosa):
        super()._init_(sabor, precio)
        self.cremosa = cremosa

    def mostrarTexturaCremosa(self):
        print(f"Textura cremosa: {'Sí' if self.cremosa else 'No'}")

    def cambiarPrecio(self):
        self.precio += 6

paleta1 = PaletaAgua("Fresa", 10, True)
paleta1.mostrarInformacion()
paleta1.mostrarBaseAgua()
paleta1.cambiarPrecio()
paleta1.mostrarInformacion()  

paleta2 = PaletaCrema("Chocolate", 12, True)
paleta2.mostrarInformacion()
paleta2.mostrarTexturaCremosa()
paleta2.cambiarPrecio()
paleta2.mostrarInformacion()