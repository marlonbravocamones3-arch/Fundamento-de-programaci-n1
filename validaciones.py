# validaciones.py - funciones de validacion de datos

def dni_valido(dni):
    """El DNI debe tener exactamente 8 digitos numericos."""
    return len(dni) == 8 and dni.isdigit()


def prioridad_de(gravedad):
    """Convierte la gravedad en numero: alta=3, media=2, baja=1."""
    if gravedad == "alta":
        return 3
    if gravedad == "media":
        return 2
    return 1


def gravedad_valida(gravedad):
    return gravedad in ("alta", "media", "baja")
