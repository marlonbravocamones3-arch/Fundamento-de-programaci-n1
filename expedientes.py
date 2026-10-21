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