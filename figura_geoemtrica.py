import math

# Clase base
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

# Clase derivada para el círculo
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

# Clase derivada para el rectángulo
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        return self.ancho * self.alto

# Clase derivada para el triángulo
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

# Ejemplo de uso
if __name__ == "__main__":
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(3, 7)

    print(f"Área del {circulo.nombre}: {circulo.calcularArea()}")
    print(f"Área del {rectangulo.nombre}: {rectangulo.calcularArea()}")
    print(f"Área del {triangulo.nombre}: {triangulo.calcularArea()}")
