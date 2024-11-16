class SistemaMaterias:
    def __init__(self):
        self.materias = set()

    def agregar_materia(self, nombre):
        if nombre in self.materias:
            raise ValueError("Materia ya registrada.")
        self.materias.add(nombre)

    def obtener_materia(self, nombre):
        if nombre not in self.materias:
            raise KeyError("Materia no encontrada.")
        return nombre

# Ejemplo de uso
sistema = SistemaMaterias()

try:
    sistema.agregar_materia("Matemáticas")
    sistema.agregar_materia("Historia")
    sistema.agregar_materia("Matemáticas")  # Excepción
except ValueError as e:
    print(e)

try:
    print(sistema.obtener_materia("Historia"))
    print(sistema.obtener_materia("Ciencias"))  # Excepción
except KeyError as e:
    print(e)
