class FiguraGeometrica:
    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        if not self._es_triangulo_valido():
            raise GeometriaInvalidaError("Los lados no forman un triángulo válido")

    def _es_triangulo_valido(self):
        # Condición del triángulo: la suma de dos lados debe ser mayor al tercer lado
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        try:
            if self.lado == 0:
                raise ZeroDivisionError("El lado no puede ser cero.")
            return 4 * self.lado
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None


class GeometriaInvalidaError(Exception):
    """Excepción lanzada cuando se intenta crear una figura con geometría imposible."""
    pass


# Pruebas
try:
    t = Triangulo(3, 4, 10)  # Esto debería lanzar una excepción
    print(t.calcular_perimetro())
except GeometriaInvalidaError as e:
    print(f"Error: {e}")

c = Cuadrado(5)
print(f"Perímetro del cuadrado: {c.calcular_perimetro()}")

