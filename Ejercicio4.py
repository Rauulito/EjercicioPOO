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

    #Metodo para obtener el saldo lo utilizaremos para ver si se puede sacar dinero y tranferir dinero
    def getSaldo(self):
            return self.saldo

    #Metodo para sacar
    def sacarDinero(self, dineroSacado):
        if(getSaldo> dineroSacado):
            self.saldo= self.saldo - dineroSacado
