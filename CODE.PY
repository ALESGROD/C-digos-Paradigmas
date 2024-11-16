class Gallina:  

    def __init__(self, numero_huevos, feliz):  

        self.__numero_huevos = numero_huevos  # Atributo privado  

        self.__feliz = feliz  # Atributo privado  

    # Método getter para numero_huevos  

    def get_numero_huevos(self):  

        return self.__numero_huevos  

    # Método setter para numero_huevos  

    def set_numero_huevos(self, nuevo_numero):  

        self.__numero_huevos = nuevo_numero  

    # Método getter para feliz  

    def is_feliz(self):  

        return self.__feliz  

    # Método setter para feliz  

    def set_feliz(self, nuevo_feliz):  

        self.__feliz = nuevo_feliz  

# Ejemplo de uso  

gallina = Gallina(10, True)  

# Accediendo a los atributos mediante getters  

print(gallina.get_numero_huevos())  # Imprime: 10  

print(gallina.is_feliz())  # Imprime: True  

# Modificando los atributos mediante setters  

gallina.set_numero_huevos(12)  

gallina.set_feliz(False)  

# Verificando los cambios  

print(gallina.get_numero_huevos())  # Imprime: 12  

print(gallina.is_feliz())  # Imprime: False  