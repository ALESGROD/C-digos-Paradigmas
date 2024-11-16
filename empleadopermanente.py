class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, num_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.num_seguro_social = num_seguro_social
    
    def calcular_ingresos(self):
        return self.sueldo_base
    
    def calcular_descuento(self):
        return self.sueldo_base * 0.11
    
    def calcular_sueldo_neto(self):
        return self.calcular_ingresos() - self.calcular_descuento()

