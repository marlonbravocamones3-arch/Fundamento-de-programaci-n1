# expedientes.py - registro de expedientes con insercion ordenada por prioridad
from validaciones import prioridad_de


def posicion_insercion(prioridad, nueva):
    """Primera posicion cuya prioridad es menor a la nueva (respeta orden de llegada)."""
    pos = 0
    while pos < len(prioridad) and prioridad[pos] >= nueva:
        pos += 1
    return pos


def registrar_expediente(codigo, nombre, dni, telefono, tipo, gravedad,
                         prioridad, estado,
                         v_nombre, v_dni, v_tel, v_tipo, v_gravedad):
    """Inserta el expediente en su posicion y devuelve el codigo generado."""
    p = prioridad_de(v_gravedad)
    pos = posicion_insercion(prioridad, p)
    cod = "EXP-" + str(1001 + len(codigo))
    codigo.insert(pos, cod)
    nombre.insert(pos, v_nombre)
    dni.insert(pos, v_dni)
    telefono.insert(pos, v_tel)
    tipo.insert(pos, v_tipo)
    gravedad.insert(pos, v_gravedad)
    prioridad.insert(pos, p)
    estado.insert(pos, "Pendiente")
    return cod


def buscar_lineal(claves, buscado):
    """Busqueda lineal: devuelve la posicion encontrada o -1 si no existe."""
    for i in range(len(claves)):
        if claves[i] == buscado:
            return i
    return -1


def mostrar_expediente(codigo, nombre, dni, telefono, tipo, gravedad, estado, i):
    print("Codigo:", codigo[i], "| Solicitante:", nombre[i],
          "| DNI:", dni[i], "| Tel:", telefono[i])
    print("Solicitud:", tipo[i], "| Gravedad:", gravedad[i], "| Estado:", estado[i])


def consultar_expediente(codigo, nombre, dni, telefono, tipo, gravedad, estado):
    buscado = input("Ingrese el codigo (EXP-xxxx) o el DNI: ").strip().upper()
    pos = buscar_lineal(codigo, buscado)
    if pos == -1:
        pos = buscar_lineal(dni, buscado)
    if pos == -1:
        print("Expediente no encontrado.")
    else:
        mostrar_expediente(codigo, nombre, dni, telefono, tipo, gravedad, estado, pos)


def listar_priorizado (codigo, nombre, dni, telefono, tipo, gravedad, estado):
    """Muestra todos los expedientes (ya estan ordenados de mayor a menor urgencia)."""
    if len(codigo) == 0:
        print("No hay expedientes registrados.")
        return
    print("===== LISTADO PRIORIZADO (de mayor a menor urgencia) =====")
    for i in range(len(codigo)):
        print(str(i + 1) + ")")
        mostrar_expediente(codigo, nombre, dni, telefono, tipo, gravedad, estado, i)
