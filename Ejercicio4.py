import random

class CuentaBancaria():
    #Atributos
    ID= 0
    titular= ""
    fechaApertura=0
    numeroCuenta=""
    saldo=0.0

    #Constructor para crear la cuenta bancaria
    def __init__(self, ID, titular, fechaApertura, numeroCuenta, saldo):
        self.ID= ID
        self.titular= titular
        self.fechaApertura= fechaApertura
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

class CuentaBancariaPlazoFijo():
    #Atributos
    ID= 0
    titular= ""
    fechaApertura=0
    numeroCuenta=0
    saldo=0.0

    #Constructor para crear la cuenta bancaria plazo fijo
    def __init__(self, ID, titular, fechaApertura, numeroCuenta, saldo):
        self.ID= ID
        self.titular= titular
        self.fechaApertura= fechaApertura
        self.numeroCuenta= numeroCuenta
        self.saldo= saldo

    def sacarDinero2(self, dinero,fVencimiento, fsalida):
        if(fsalida>=fVencimiento):
            self.saldo= self.saldo - dinero
        else:
            dinero= dinero+ dinero*0.05  #Penalizacion del 5& por retirar dinero antes de la fecha de vencimiento
            self.saldo= self.saldo - dinero
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

class CuentaVip():
    #Atributos
    ID= 0
    titular= ""
    fechaApertura=0
    numeroCuenta=0
    saldo=0.0
    dineroNegativo=0

    #Constructor para crear la cuenta bancaria vip
    def __init__(self, ID, titular, fechaApertura, numeroCuenta, saldo, maxDineroNegativo):
        self.ID= ID
        self.titular= titular
        self.fechaApertura= fechaApertura
        self.numeroCuenta= numeroCuenta
        self.saldo= saldo
        self.maxDineroNegativo= maxDineroNegativo
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

#ID es un entero incremental, es decir, va incrementando en uno para cada cuenta que se cree
#Fecha de apertura numero aleatrio entre 1900 y 2021
#Número de cuenta es un número aleatorio de 12 digitos
cuentaBancaria =  CuentaBancaria(int(1000),"Juan",int(random.randint(1900,2021)),int(random.randint(100000000000,999999999999)),float(10000))
print("Cuenta Bancaria:")
print(cuentaBancaria.ID,cuentaBancaria.titular,cuentaBancaria.fechaApertura,cuentaBancaria.numeroCuenta,cuentaBancaria.saldo)
cuentaBancariaPlazoFijo =  CuentaBancariaPlazoFijo(int(1001),"Pedro",int(random.randint(1900,2021)),int(random.randint(100000000000,999999999999)),float(10000))
print("Cuenta Bancaria a plazo fijo:")
print(cuentaBancariaPlazoFijo.ID,cuentaBancariaPlazoFijo.titular,cuentaBancariaPlazoFijo.fechaApertura,cuentaBancariaPlazoFijo.numeroCuenta,cuentaBancariaPlazoFijo.saldo)
cuentaVip =  CuentaVip(int(1002),"Raul",int(random.randint(1900,2021)),int(random.randint(100000000000,999999999999)),float(10000),float(-3000))
print("Cuenta Vip")
print(cuentaVip.ID,cuentaVip.titular,cuentaVip.fechaApertura,cuentaVip.numeroCuenta,cuentaVip.saldo,cuentaVip.maxDineroNegativo)

#Probamos metodos de meter en cuenta bancaria y cuenta vip
print("En la cuenta bancaria tras sacar dinero queda:")
cuentaBancaria.sacarDinero(78)
print(cuentaBancaria.ID,cuentaBancaria.titular,cuentaBancaria.fechaApertura,cuentaBancaria.numeroCuenta,cuentaBancaria.saldo)

#Probamos metodo para sacar dinero de la cuenta bancaria a plazo fijo
print("En la cuenta bancaria a plazo fijo tras sacar dinero queda:")
cuentaBancariaPlazoFijo.sacarDinero2(78,random.randint(2022,2099),2021)
print(cuentaBancariaPlazoFijo.ID,cuentaBancariaPlazoFijo.titular,cuentaBancariaPlazoFijo.fechaApertura,cuentaBancariaPlazoFijo.numeroCuenta,cuentaBancariaPlazoFijo.saldo)

#Probamos metodo para meter dinero que es el mismo en las tres cuentas
print("En la cuenta bancaria tras meter dinero queda:")
cuentaBancaria.meterDinero(575)
print(cuentaBancaria.ID,cuentaBancaria.titular,cuentaBancaria.fechaApertura,cuentaBancaria.numeroCuenta,cuentaBancaria.saldo)

#Probamos metodo de transferir dinero que es el mismo para las tres cuentas
cuentaBancaria.transferirDinero(2000,cuentaVip)
print("En la cuenta bancaria tras tranferir dinero queda:")
print(cuentaBancaria.ID,cuentaBancaria.titular,cuentaBancaria.fechaApertura,cuentaBancaria.numeroCuenta,cuentaBancaria.saldo)
print("En la cuenta vip tras haberle transferido dinero queda:")
print(cuentaVip.ID,cuentaVip.titular,cuentaVip.fechaApertura,cuentaVip.numeroCuenta,cuentaVip.saldo,cuentaVip.maxDineroNegativo)