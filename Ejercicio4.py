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
        if(self.getSaldo()>= dineroSacado):
            self.saldo= self.saldo - dineroSacado
        else:
            print("No hay suficiente dinero en la cuenta")
    #Metodo para meter
    def meterDinero(self, dineroMetido):
        self.saldo= self.saldo + dineroMetido

    #Metodo para transferir
    def transferirDinero(self, dinero,cuantaTransferida):
        if(self.getSaldo()>= dinero):
            self.sacarDinero(dinero)
            cuantaTransferida.meterDinero(dinero)
        else:
            print("No hay dinero suficiente")