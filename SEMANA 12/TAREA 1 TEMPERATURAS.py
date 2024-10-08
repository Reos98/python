# Definir la matriz 3D de temperaturas (modificada) modificacion de codigo de la semana 12
temperaturas = [
    [   # Ciudad 1
        [78, 80, 82, 79, 85, 88, 92],  # Semana 1
        [76, 79, 83, 81, 87, 89, 93],  # Semana 2
        [77, 81, 85, 82, 88, 91, 95],  # Semana 3
        [75, 78, 80, 79, 84, 87, 91]   # Semana 4
    ],
    [   # Ciudad 2
        [72, 74, 78, 70, 73, 75, 79],  # Semana 1 (modificada)
        [73, 66, 70, 72, 75, 77, 81],  # Semana 2 (modificada)
        [71, 65, 68, 70, 72, 76, 80],  # Semana 3 (modificada)
        [74, 67, 69, 71, 74, 77, 80]   # Semana 4 (modificada)
    ],
    [   # Ciudad 3
        [90, 92, 94, 91, 88, 85, 82],  # Semana 1
        [89, 91, 93, 90, 87, 84, 81],  # Semana 2
        [91, 93, 95, 92, 89, 86, 83],  # Semana 3
        [88, 90, 92, 89, 86, 83, 80]   # Semana 4
    ]
]

# Cambiar los valores que no están en el rango [70, 90] (modificado)
for ciudad in temperaturas:
    for semana in ciudad:
        for index in range(len(semana)):
            if semana[index] < 70:
                semana[index] = 70
            elif semana[index] > 90:
                semana[index] = 90

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")
    for j, semana in enumerate(ciudad):
        suma = sum(semana)  # Sumar todas las temperaturas de la semana
        promedio = suma / len(semana)  # Calcular el promedio
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}")