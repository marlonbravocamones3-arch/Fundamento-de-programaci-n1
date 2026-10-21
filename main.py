# main.py - Mesa de partes digital en salud (prototipo)
# Listas paralelas: la posicion i de cada lista es el mismo expediente
codigo, nombre, dni, telefono = [], [], [], []
tipo, gravedad, prioridad, estado = [], [], [], []


def mostrar_menu():
    print("\n===== MESA DE PARTES DIGITAL EN SALUD =====")
    print("1. Registrar solicitud")
    print("2. Consultar expediente (por codigo o DNI)")
    print("3. Ver listado priorizado")
    print("4. Salir")


opcion = 0
while opcion != 4:
    mostrar_menu()
    entrada = input("Elija una opcion: ")
    if not entrada.isdigit():
        print("Opcion invalida.")
        continue
    opcion = int(entrada)
    if opcion == 1:
        print("Registro en construccion")
    elif opcion == 2:
        print("Consulta en construccion")
    elif opcion == 3:
        print("Listado en construccion")
    elif opcion == 4:
        print("Fin del programa.")
    else:
        print("Opcion invalida.")