# main.py - Mesa de partes digital en salud (prototipo)
# Listas paralelas: la posicion i de cada lista es el mismo expediente
codigo, nombre, dni, telefono = [], [], [], []
tipo, gravedad, prioridad, estado = [], [], [], []
from validaciones import dni_valido, gravedad_valida
from expedientes import registrar_expediente, consultar_expediente, listar_priorizado


def mostrar_menu():
    print("\n===== MESA DE PARTES DIGITAL EN SALUD =====")
    print("1. Registrar solicitud")
    print("2. Consultar expediente (por codigo o DNI)")
    print("3. Ver listado priorizado")
    print("4. Salir")

def pedir_y_registrar():

 v_nombre = input("Nombre completo: ").strip()
 while v_nombre == "":
            v_nombre = input("El nombre no puede estar vacio: ").strip()
 v_dni = input("DNI (8 digitos): ")
 while not dni_valido(v_dni):
            v_dni = input("DNI invalido. Debe tener 8 digitos numericos: ")
 v_tel = input("Telefono de contacto: ")
 tipos = ["Atencion medica de urgencia", "Medicamentos", "Ambulancia",
                 "Personal sanitario", "Apoyo estructural"]
 print("Tipo: 1=Atencion urgente 2=Medicamentos 3=Ambulancia "
              "4=Personal sanitario 5=Apoyo estructural")
 n = input("Elija 1 a 5: ")
 while not (n.isdigit() and 1 <= int(n) <= 5):
            n = input("Tipo invalido. Elija 1 a 5: ")
 v_gravedad = input("Gravedad (alta/media/baja): ").lower()
 while not gravedad_valida(v_gravedad):
            v_gravedad = input("Escriba alta, media o baja: ").lower()
 cod = registrar_expediente(codigo, nombre, dni, telefono, tipo, gravedad,
                                   prioridad, estado, v_nombre, v_dni, v_tel,
                                   tipos[int(n) - 1], v_gravedad)
 print("Expediente registrado. Codigo de confirmacion:", cod)
opcion = 0
while opcion != 4:
    mostrar_menu()
    entrada = input("Elija una opcion: ")
    if not entrada.isdigit():
        print("Opcion invalida.")
        continue
    opcion = int(entrada)
    if opcion == 1:             
     pedir_y_registrar()
    elif opcion == 2:
        consultar_expediente(codigo, nombre, dni, telefono, tipo, gravedad, estado)
    elif opcion == 3:
        listar_priorizado(codigo, nombre, dni, telefono, tipo, gravedad, estado)
    elif opcion == 4:
        print("Fin del programa.")
    else:
        print("Opcion invalida.")