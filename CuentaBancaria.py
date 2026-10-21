from abc import ABC, abstractmethod

class SaldoInsuficiente(Exception):
    pass

class cuentaBancaria (ABC):
    def __init__(self,numeroDeCuenta,saldo:float):
        self.numeroDeCuenta = numeroDeCuenta
        self.saldo = saldo 
    
    
    def retirarMonto(self):
        print("Ingrese el monto a retirar")
        monto = int(input())
    
        if monto > self.saldo:
            raise SaldoInsuficiente("El monto a retirar es mayor que el saldo")
    
        else:
            self.saldo = self.saldo-monto
            print("Retiro exitoso")
            print("El saldo actual de la cuenta", self.numeroDeCuenta, "seria", self.saldo)        
    
   
