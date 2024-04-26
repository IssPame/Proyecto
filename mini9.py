import numpy as np

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def obtener_coeficientes(mensaje, num_variables):
    coeficientes = []
    for i in range(num_variables):
        while True:
            try:
                coeficiente = float(input(f"Ingrese el coeficiente para la variable x{i+1} en {mensaje}: "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")

        coeficientes.append(coeficiente)
    return coeficientes

def crear_matriz(num_variables, num_restricciones, coeficientes_objetivo, coeficientes_restricciones, tipo_problema):
    num_total_variables = num_variables + num_restricciones
    matriz = np.zeros((num_restricciones + 1, num_total_variables + num_restricciones + 1))

    if tipo_problema == 'min':
        coeficientes_objetivo = [-coeficiente for coeficiente in coeficientes_objetivo]

    matriz[0, :num_variables] = coeficientes_objetivo
    matriz[0, num_variables:num_total_variables] = 0
    matriz[0, -1] = 0

    for i in range(num_restricciones):
        matriz[i + 1, :num_variables] = coeficientes_restricciones[i][:-2]
        signo_restriccion = coeficientes_restricciones[i][-2]
        if signo_restriccion == '<=':
            matriz[i + 1, num_variables + i] = 1
        elif signo_restriccion == '>=':
            matriz[i + 1, num_variables + num_restricciones + i] = -1
            matriz[i + 1, num_variables + i] = 1
        elif signo_restriccion == '=':
            matriz[i + 1, num_variables + num_restricciones + i] = 1
        matriz[i + 1, -1] = coeficientes_restricciones[i][-1]

    return matriz

def encontrar_columna_pivote(matriz):
    num_filas, num_columnas = matriz.shape
    columna_pivote = np.argmax(matriz[0, :-1])
    return columna_pivote

def encontrar_fila_pivote(matriz, columna_pivote):
    num_filas = matriz.shape[0]
    ratios = []
    for i in range(1, num_filas):
        if matriz[i, columna_pivote] > 0:
            ratio = matriz[i, -1] / matriz[i, columna_pivote]
            ratios.append((i, ratio))
    if ratios:
        return min(ratios, key=lambda x: x[1])[0]
    else:
        return None

def iteracion_simplex(matriz):
    columna_pivote = encontrar_columna_pivote(matriz)
    fila_pivote = encontrar_fila_pivote(matriz, columna_pivote)
    if fila_pivote is not None:
        elemento_pivote = matriz[fila_pivote, columna_pivote]
        matriz[fila_pivote, :] /= elemento_pivote
        for i in range(matriz.shape[0]):
            if i != fila_pivote:
                factor = matriz[i, columna_pivote]
                matriz[i, :] -= factor * matriz[fila_pivote, :]
        return matriz
    else:
        return None

def imprimir_matriz(matriz):
    print("\nMatriz:")
    print(matriz)

def resolver_simplex(num_variables, num_restricciones, coeficientes_objetivo, coeficientes_restricciones, tipo_problema):
    matriz = crear_matriz(num_variables, num_restricciones, coeficientes_objetivo, coeficientes_restricciones, tipo_problema)
    imprimir_matriz(matriz)
    print("\nResolviendo usando el algoritmo Simplex:")
    while True:
        matriz = iteracion_simplex(matriz)
        if matriz is not None:
            imprimir_matriz(matriz)
            if min(matriz[0, :-1]) >= 0:
                print("\nSolución óptima encontrada.")
                if tipo_problema == 'min':
                    print("Valor de la función objetivo (minimizado):", -matriz[0, -1]) # Multiplicamos por -1 para inversión de minimización
                else:
                    print("Valor de la función objetivo (maximizado):", matriz[0, -1])
                for i in range(num_variables):
                    print(f"Valor de x{i+1}:", matriz[0, i+1])
                break
        else:
            print("\nNo se puede realizar más iteraciones.")
            break

def ejecutar_iteracion_simplex_unica(matriz):
    imprimir_matriz(matriz)
    print("\nEjecutando una sola iteración del algoritmo Simplex:")
    matriz = iteracion_simplex(matriz)
    if matriz is not None:
        imprimir_matriz(matriz)
        
        # Imprimir el valor de la función objetivo
        print("\nValor de la función objetivo:", matriz[0, -1])
        
        # Imprimir los valores de las variables x1 y x2
        for i in range(num_variables):
            print(f"Valor de x{i+1}:", matriz[0, i+1])
    else:
        print("No se puede realizar más iteraciones.")

# Solicitar al usuario el número de variables y restricciones
num_variables = obtener_numero("Ingrese el número de variables en la función objetivo: ")
num_restricciones = obtener_numero("Ingrese el número de restricciones: ")

# Solicitar los coeficientes de la función objetivo
coeficientes_objetivo = obtener_coeficientes("la función objetivo", num_variables)

# Crear automáticamente las restricciones con las variables de holgura, exceso o artificiales
coeficientes_restricciones = []
for i in range(num_restricciones):
    coeficientes_restriccion = obtener_coeficientes(f"la restricción {i+1}", num_variables)
    signo_restriccion = input("Ingrese el signo de la restricción (<=, >=, =): ")
    coeficientes_restriccion.append(signo_restriccion)
    coeficientes_restriccion.append(float(input("Ingrese el término independiente de la restricción: ")))
    coeficientes_restricciones.append(coeficientes_restriccion)

# Determinar si se está maximizando o minimizando
tipo_problema = input("¿Está maximizando o minimizando? (max/min): ")

# Resolver usando el algoritmo Simplex
ejecutar_iteracion_simplex_unica(crear_matriz(num_variables, num_restricciones, coeficientes_objetivo, coeficientes_restricciones, tipo_problema))
