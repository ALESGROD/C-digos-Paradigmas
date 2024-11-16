class EmpleadoVendedor(Empleado):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
    
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
    
    def calcular_bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return self.calcular_ingresos() * 0.05
        else:
            return self.calcular_ingresos() * 0.10
    
    def calcular_descuento(self):
        if self.calcular_ingresos() < 1000:
            return self.calcular_ingresos() * 0.11
        else:
            return self.calcular_ingresos() * 0.15
    
    def calcular_sueldo_neto(self):
        return self.calcular_ingresos() + self.calcular_bonificacion() - self.calcular_descuento()


