posicion_x = 0

def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Avanzó {pasos} pasos. Posición actual: {posicion_x}")

def abajo():
    print("Bajó una línea")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
