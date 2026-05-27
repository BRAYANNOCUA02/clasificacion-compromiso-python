# MATRIZ DE DATOS
sesiones = [
    ["C001", 200, 10],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 50, 7]
]

# FUNCION PARA CLASIFICAR EL COMPROMISO
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"

# INFORME FINAL
print("===== INFORME DE COMPROMISO =====")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Clasificación:", clasificacion)
    print("---------------------------")