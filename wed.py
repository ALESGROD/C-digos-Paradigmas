from abc import ABC, abstractmethod

# Definición de la clase abstracta Habilidades
class Habilidades(ABC):
    @abstractmethod
    def ejecutar_habilidad(self):
        pass

# Definición de la clase abstracta Personaje
class Personaje(ABC):
    def _init_(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    @abstractmethod
    def atacar(self):
        pass

# Clase HabilidadesTecnologicas que hereda de Habilidades
class HabilidadesTecnologicas(Habilidades):
    def _init_(self, habilidad_tecnologica):
        self.habilidad_tecnologica = habilidad_tecnologica

    def ejecutar_habilidad(self):
        print(f"Ejecutando habilidad tecnológica: {self.habilidad_tecnologica}")

# Clase HabilidadesCiberneticas que hereda de Habilidades
class HabilidadesCiberneticas(Habilidades):
    def _init_(self, habilidad_cibernetica):
        self.habilidad_cibernetica = habilidad_cibernetica

    def ejecutar_habilidad(self):
        print(f"Usando habilidad cibernética: {self.habilidad_cibernetica}")

# Clase Androide que hereda de Personaje
class Androide(Personaje):
    def _init_(self, nombre, nivel, habilidad_tecnologica):
        super()._init_(nombre, nivel)
        self.habilidad_tecnologica = HabilidadesTecnologicas(habilidad_tecnologica)

    def atacar(self):
        print(f"{self.nombre} lanza un ataque con láser.")

    def usar_habilidad_tecnologica(self):
        self.habilidad_tecnologica.ejecutar_habilidad()

# Clase Ciborg que hereda de Personaje
class Ciborg(Personaje):
    def _init_(self, nombre, nivel, habilidad_cibernetica):
        super()._init_(nombre, nivel)
        self.habilidad_cibernetica = HabilidadesCiberneticas(habilidad_cibernetica)

    def atacar(self):
        print(f"{self.nombre} realiza un ataque de alta precisión con su brazo robótico.")

    def usar_habilidad_cibernetica(self):
        self.habilidad_cibernetica.ejecutar_habilidad()

# Clase NeoGuerrero que combina habilidades tecnológicas y cibernéticas
class NeoGuerrero(Personaje):
    def _init_(self, nombre, nivel, habilidad_tecnologica, habilidad_cibernetica):
        super()._init_(nombre, nivel)
        self.habilidad_tecnologica = HabilidadesTecnologicas(habilidad_tecnologica)
        self.habilidad_cibernetica = HabilidadesCiberneticas(habilidad_cibernetica)

    def atacar(self):
        print(f"{self.nombre} ataca usando tanto tecnología avanzada como implantes cibernéticos.")

    def usar_habilidad_tecnologica(self):
        self.habilidad_tecnologica.ejecutar_habilidad()

    def usar_habilidad_cibernetica(self):
        self.habilidad_cibernetica.ejecutar_habilidad()

# Ejecución del código principal
if __name__ == "_main_":
    androide = Androide("T-800", 10, "Rayo Láser")
    ciborg = Ciborg("Robocop", 12, "Visión Térmica")
    neo_guerrero = NeoGuerrero("Matrix", 15, "Hackeo Avanzado", "Reflejos Mejorados")

    androide.atacar()
    androide.usar_habilidad_tecnologica()

    ciborg.atacar()
    ciborg.usar_habilidad_cibernetica()

    neo_guerrero.atacar()
    neo_guerrero.usar_habilidad_tecnologica()
    neo_guerrero.usar_habilidad_cibernetica()
