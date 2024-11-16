from abc import ABC, abstractmethod

# Clase base
class Personaje(ABC):
    def _init_(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def atacar(self):
        pass
    
    @abstractmethod
    def defender(self):
        pass

# Subclase Guerrrero
class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} ataca con espada!"
    
    def defender(self):
        return f"{self.nombre} defiende con escudo!"

# Subclase Mago
class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza un hechizo!"
    
    def defender(self):
        return f"{self.nombre} conjura un escudo mágico!"

# Subclase Arquero
class Arquero(Personaje):
    def atacar(self):
        return f"{self.nombre} dispara una flecha!"
    
    def defender(self):
        return f"{self.nombre} esquiva con agilidad!"

# Funcion para mostrar acciones
def mostrar_acciones(personaje):
    print(personaje.atacar())
    print(personaje.defender())

# Creación de instancias y uso del polimorfismo
guerrero = Guerrero("Aragorn")
mago = Mago("Gandalf")
arquero = Arquero("Legolas")

mostrar_acciones(guerrero)
mostrar_acciones(mago)
mostrar_acciones(arquero)