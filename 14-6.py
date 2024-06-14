class CajaDeAhorro:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def mostrar_saldo(self):
        print(f"El saldo actual es: ${self.saldo:.2f}")

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def extraccion(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han extraído ${cantidad:.2f}")
            else:
                print("No hay suficiente saldo para realizar la extracción.")
        else:
            print("La cantidad a extraer debe ser positiva.")

# Inicialización de la cuenta con saldo inicial proporcionado por el usuario
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
cuenta = CajaDeAhorro(saldo_inicial)

# Mostrar saldo inicial
cuenta.mostrar_saldo()

while True:
    print("\n¿Qué operación desea realizar?")
    print("1. Depositar dinero")
    print("2. Extraer dinero")
    print("3. Mostrar saldo")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.deposito(cantidad)
        cuenta.mostrar_saldo()
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a extraer: "))
        cuenta.extraccion(cantidad)
        cuenta.mostrar_saldo()
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        print("Gracias por usar la aplicación.")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
