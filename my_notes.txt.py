# Escritura de Archivo de Texto
def escribir_archivo():
    # Crea un nuevo archivo llamado my_notes.txt
    archivo = open("my_notes.txt", "w")

    # Escribe al menos tres líneas de notas personales en el archivo
    archivo.write("Nota 1: Soy una persona gamer.\n")
    archivo.write("Nota 2: He gastado dinero en la tienda de steam.\n")
    archivo.write("Nota 3: Me compre la consola xbox series S.\n")

    # Cierra el archivo
    archivo.close()


# Lectura de Archivo de Texto
def leer_archivo():
    # Abre el archivo my_notes.txt
    archivo = open("my_notes.txt", "r")

    # Lee el contenido del archivo línea por línea utilizando el método adecuado
    linea = archivo.readline()
    while linea:
        # Muestra en la consola cada línea leída
        print(linea.strip())
        linea = archivo.readline()

    # Cierra el archivo
    archivo.close()


# Llama a las funciones
escribir_archivo()
leer_archivo()