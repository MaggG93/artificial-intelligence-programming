import random
import xml.etree.ElementTree as ET

# Lee los archivos XML y los convierte en diccionarios
def cargar_xml(ruta_xml, etiqueta):
    datos = {}
    for elemento in ET.parse(ruta_xml).getroot().findall(etiqueta):
        clave = (elemento.get("choice"), elemento.get("against"))
        datos[clave] = elemento.text
    return datos

# Carga las jugadas y los mensajes al ejecutar el programa
victorias = cargar_xml("victories.xml", "victory")
derrotas = cargar_xml("defeats.xml", "defeat")

# Lista de jugadas posibles
opciones = list(dict.fromkeys(ganador for ganador, _ in victorias))

# Menú de juego
def pedir_jugada():
    for numero, opcion in enumerate(opciones):
        print(f"{numero} - {opcion}")
    seleccion = int(input("Elige una opción: "))
    return opciones[seleccion]

# Ronda de juego
def jugar_ronda():
    usuario = pedir_jugada()
    maquina = random.choice(opciones)
    print(f"Tú elegiste {usuario} y la máquina eligió {maquina}.")

    if usuario == maquina:
        print("Usuario y máquina han empatado.")
    elif (usuario, maquina) in victorias:
        print(victorias[(usuario, maquina)])
    else:
        print(derrotas[(usuario, maquina)])

def main():
    # Bucle principal
    while True:
        try:
            jugar_ronda()
        except (ValueError, IndexError):
            print("Opción no válida.")
            continue

        if input("¿Jugar otra ronda? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    main()