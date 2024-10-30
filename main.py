def contar_objetos(imagen, fondo=240, tolerancia=15):
    filas, columnas = len(imagen), len(imagen[0])
    etiquetas = [[0] * columnas for _ in range(filas)]  # Matriz de etiquetas
    etiqueta_actual = 0  # Para asignar etiquetas a objetos

    # Función de DFS para etiquetar componentes conectados
    def dfs(x, y, etiqueta):
        stack = [(x, y)]
        while stack:
            i, j = stack.pop()
            if etiquetas[i][j] != 0:  # Si ya está etiquetado, saltar
                continue
            etiquetas[i][j] = etiqueta  # Asignar etiqueta

            # Explorar vecinos (arriba, abajo, izquierda, derecha)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < filas and 0 <= nj < columnas:
                    # Si el vecino está dentro de la tolerancia y sin etiquetar
                    if etiquetas[ni][nj] == 0 and abs(imagen[ni][nj] - imagen[i][j]) <= tolerancia:
                        if imagen[ni][nj] < fondo:  # Comprobar que no es fondo
                            stack.append((ni, nj))

    # Recorrer cada píxel de la imagen
    for i in range(filas):
        for j in range(columnas):
            # Si el píxel no es fondo y no está etiquetado
            if imagen[i][j] < fondo and etiquetas[i][j] == 0:
                etiqueta_actual += 1  # Nueva etiqueta para un nuevo objeto
                dfs(i, j, etiqueta_actual)  # Etiquetar el objeto

    return etiqueta_actual  # Número total de objetos


# Solicitar la entrada completa de la matriz de la imagen al usuario
print("Ingrese la matriz completa de la imagen en escala de grises, fila por fila.")
print("Cada fila debe estar en una nueva línea y los valores separados por comas.")
print("Cuando termine de ingresar todas las filas, presione Enter." + '\n')

# Leer todas las filas en una sola entrada y dividirlas por líneas
imagen = []
while True:
    fila = input()
    if not fila:
        break
    # Convertir la fila ingresada en una lista de enteros
    imagen.append([int(valor) for valor in fila.split(",")])

# Verificar que la imagen no esté vacía y tenga filas del mismo tamaño
if not imagen or any(len(fila) != len(imagen[0]) for fila in imagen):
    print("Error: La matriz debe ser no vacía y todas las filas deben tener el mismo número de elementos.")
else:
    # Calcular y mostrar el número de objetos
    print("Número de objetos:", contar_objetos(imagen))

