# Excepciones personalizadas
class NivelInvalidoError(Exception):
    def __init__(self, mensaje="El nivel no puede ser menor que 1."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class AtaqueNoPermitidoError(Exception):
    def __init__(self, mensaje="El nivel debe ser al menos 5 para atacar."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Clase base Personaje
class Personaje:
    def __init__(self, nombre, nivel):
        if nivel < 1:
            raise NivelInvalidoError()
        self.nombre = nombre
        self.nivel = nivel

    def atacar(self):
        if self.nivel < 5:
            raise AtaqueNoPermitidoError()
        print(f"{self.nombre} está atacando.")

# Subclase Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
    
    def atacar(self):
        super().atacar()
        print(f"El guerrero {self.nombre} lanza un ataque con su espada.")

# Subclase Mago
class Mago(Personaje):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
    
    def atacar(self):
        super().atacar()
        print(f"El mago {self.nombre} lanza un hechizo de fuego.")

# Ejemplos de uso y manejo de excepciones
try:
    personaje1 = Guerrero("Thor", 0)  # Esto lanzará una excepción NivelInvalidoError
except NivelInvalidoError as e:
    print(f"Error al crear el personaje: {e}")

try:
    personaje2 = Mago("Gandalf", 3)
    personaje2.atacar()  # Esto lanzará una excepción AtaqueNoPermitidoError
except AtaqueNoPermitidoError as e:
    print(f"Error al atacar: {e}")

try:
    personaje3 = Guerrero("Aragorn", 5)
    personaje3.atacar()  # Esto funcionará sin problemas
except (NivelInvalidoError, AtaqueNoPermitidoError) as e:
    print(f"Error: {e}")

