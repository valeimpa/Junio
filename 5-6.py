class Objeto:
    def __init__(self, propiedad):
        self.propiedad = propiedad

objeto = None

while True:
    print("\nMenú:")
    print("1. Cargar un objeto")
    print("2. Modificar la propiedad del objeto")
    print("3. Borrar el objeto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        if objeto is None:
            valor_propiedad = input("Ingrese el valor de la propiedad: ")
            objeto = Objeto(valor_propiedad)
            print(f"Objeto creado con la propiedad: {objeto.propiedad}")
        else:
            print("Ya hay un objeto cargado.")

    elif opcion == '2':
        if objeto is not None:
            nuevo_valor = input("Ingrese el nuevo valor de la propiedad: ")
            objeto.propiedad = nuevo_valor
            print(f"Propiedad modificada: {objeto.propiedad}")
        else:
            print("No hay ningún objeto cargado.")

    elif opcion == '3':
        if objeto is not None:
            objeto = None
            print("Objeto borrado.")
        else:
            print("No hay ningún objeto para borrar.")

    elif opcion == '4':
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
