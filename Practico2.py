#Scrip implementar clase CuentaBancaria. Atributos: Titular, Nº Cuenta, Saldo. Metodos: Ingresos , retirar dinero, consultar saldo y movimientos. Saldo 0 no puede retirar dinero.

import random

class CuentaBancaria:
    def __init__(self, titular, num_cuenta, saldo_inicial=0 ):
        self.titular = titular
        self.nºcuenta = num_cuenta
        self.saldo = saldo_inicial
        self.movimientos = []

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append(f"Ingreso: +{cantidad}€")
            print(f"Se han ingresado {cantidad}€")
            print(f"El saldo de tu cuenta actual es: {self.saldo}")
        else:
            print("La cantidad ha ingresar debe ser positiva.")
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad ha retirar debe ser positiva")
        elif cantidad > self.saldo:
            print("Saldo insuficiente. No puede retirar dinero.")
        else:
            self.saldo -= cantidad
            self.movimientos.append(f"Retirar: -{cantidad}€")
            print(f"Se han retirado {cantidad}€")
            print(f"Su saldo actual es de: {self.saldo}")

    def consultar_saldo(self):
        print (f"Su saldo actual es de {self.saldo}")
        return self.saldo
    
    def ver_movimientos(self):
        print("\n Movimientos en la cueta:")
        if not self.movimientos:
            print("No hay movimientos")
        else:
            for mov in self.movimientos:
                print(mov)


 #Creamos lista con las cuentas.

cuentas = []

#Creamos la funcion que busca las cuentas.

def buscar_cuenta(nombre, numero):
    for cuenta in cuentas:
        if cuenta.titular == nombre and cuenta.numero_cuenta == numero:
            return cuenta
    return None

#Creamos funcion asigna numero cuenta random

def generar_num_cuenta():
    return str(random.randint(1000000,999999999))

print("Bienvenido al servicio bancario \n")

es_usuario = input("¿Es usted usuario? S/N: \n").upper()

if es_usuario == str("S"):
    nombre = str(input("Introduzca su nombre: "))
    numero = int(input("Introduzca su numero de cuenta: "))

    cuenta = buscar_cuenta(nombre, numero)

    if cuenta:
        print(f"Bienvenido {nombre}")
    else:
        print("Este usuario no existe.")
        crear = str(input("Desea crear un nuevo usuario? S/N \n").upper())
        
        if crear == str("S"):
            print("Creando nuevo usuario...")
            nombre_nuevo = input("Introduce tu nombre: \n")
            numero_nuevo = generar_num_cuenta()

            cuenta = CuentaBancaria(nombre_nuevo, numero_nuevo, saldo_inicial=200)
            cuentas.append(cuenta)


            print("La cuenta ha sido creada correctamente.")
            print(f"Titular: {nombre_nuevo}")
            print(f"Número de cuenta: {numero_nuevo}")
            print(f"Saldo inicial: 200€")
        
        else:
            print("Saliendo del sistema.")
            exit()

else:
    crear = input("¿Desea crear un nuevo usuario? S/N ")
    if crear == "S":
        print("Creadno nuevo usuario...")
        nombre_nuevo = input("Introduce tu nombre: \n")
        numero_nuevo = generar_num_cuenta()

        cuenta = CuentaBancaria(nombre_nuevo,numero_nuevo, saldo_inicial=200)
        cuentas.append(cuenta)

        print("La cuenta ha sido creada correctamente.")
        print(f"Titular: {nombre_nuevo}")
        print(f"Numero de cuenta: {numero_nuevo}")
        print("Saldo inicial: 200")
    else:
        print("Saliendo del sistema \n")
        print("Gracias")

#Menu de operacionnes

while True:
    print("¿Que quieres hacer?")
    print("-- Menu --")
    print("1 - Ingresar")
    print("2 - Retirar dinero")
    print("3 - Consultar saldo")
    print("4 - Consultar movimientos")
    print("5 - Salir")

    opcion = int(input("Selecione una opcion: "))

    if opcion == int("1"):
        cantidad = float(input("Cantidad a ingresar: "))
        cuenta.ingresar(cantidad)
    elif opcion == int("2"):
        cantidad = float(input("Cantidad que desea retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == int("3"):
        cuenta.consultar_saldo()
    elif opcion == int("4"):
        cuenta.ver_movimientos()
    elif opcion == int(5):
        print("Gracias por visitarnos.")
        break
    else:
        print("La opcion elegida no existe.")