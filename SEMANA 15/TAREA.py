# Crear un diccionario llamado informacion_personal con claves: "nombre", "edad", "ciudad", y "profesion"
informacion_personal = {
    "nombre": "Byron Montoya",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Militar en Servicio Activo"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Napo"  # Modificamos la ciudad de Quito a Guayaquil

# Agregar una nueva clave-valor que represente la "profesion" (en este caso ya está, pero si fuera necesario)
informacion_personal["profesion"] = "Policia"  # Modificamos la profesión de Ingeniero a Arquitecto

# Verificar si la clave "telefono" existe en el diccionario. Si no, agregarla con un valor ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0962115658"  # Agregamos un número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]  # Eliminamos la clave edad ya que no es necesaria

# Imprimir el diccionario final utilizando un bucle for
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")