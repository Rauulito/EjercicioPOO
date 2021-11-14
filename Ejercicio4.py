class CuentaBanacaria():
    #Atributos
    ID= 0
    titular= ""
    fechaApertura=0
    numeroCuenta=0
    saldo=0.0

    #Constructor para crear la cuenta bancaria
    def __init__(self, ID, titular, fechaApertura, numeroCuenta, saldo):
        self.ID= ID
        self.titular= titular
        self.fechaApertra= fechaApertura
        self.numeroCuenta= numeroCuenta
        self.saldo= saldo

    #Metodo para sacar
    def sacarDinero(self, dineroSacado):
        self.saldo=  self.saldo- dineroSacado

    #Metodo para meter
    def meterDinero(self, dineroMetido):
        self.saldo=  self.saldo + dineroMetido

    #Metodo para traspasar
    def traspasarDinero(self,dinero,cuenta1,cuenta2):
