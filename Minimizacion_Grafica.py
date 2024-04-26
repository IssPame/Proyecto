# Librerias necesarias
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definicion de simbolos
x, y = sp.symbols('x, y')

# Funcion para validar el operador de la inecuacion
# Raise interrumpe el programa y activa el manejo de excepciones
def Validar_Op(op):
    Op_Validos = ['<=', '<', '=', '>', '>=']
    if op not in Op_Validos:
        raise ValueError(f"Ingrese un operador valido {Op_Validos}")
    return op

# Funcion para validar numeros
def Validar_Num(msj):
    while True:
        try:
            num = float(input(msj))
            return num
        except ValueError:
            print("Por favor ingrese un numero valido")

# Solicitud de datos de la funcion objetivo
F_Obj_x = Validar_Num("Indique el valor de X1 en la funcion objetivo: ")
F_Obj_y = Validar_Num("Indique el valor de X2 en la funcion objetivo: ")
Z = F_Obj_x*x + F_Obj_y*y
print("La función objetivo es: Z = ", Z)
print()

# Solicitud de datos de las restricciones
Restricciones = Validar_Num("Indique el numero de restricciones: ")
Restricciones = int(Restricciones)
restricciones = []

for i in range(Restricciones):
    print()
    Ec_x = Validar_Num(f"Indique el valor de X1 en la restriccion {i+1}: ")
    Ec_y = Validar_Num(f"Indique el valor de X2 en la restriccion {i+1}: ")
    Tipo = input("Indique el tipo de restriccion (<=, <, =, >, >=): ")
    while Tipo not in ['<=', '<', '=', '>', '>=']:
        print("Operador inválido. Intente de nuevo.")
        Tipo = input("Indique el tipo de restricción (<=, <, =, >, >=): ")
    Tipo = Validar_Op(Tipo)
    ValorEc = Validar_Num(f"Indique el valor de la restriccion {i+1}: ")
    restricciones.append((Ec_x, Ec_y, Tipo, ValorEc))
print()

for i, (Ec_x, Ec_y, Tipo, ValorEc) in enumerate(restricciones, start=1):
    print(f"Restriccion {i}: {Ec_x}*x1 + {Ec_y}*x2 {Tipo} {ValorEc}")
print()

# Transformacion de inecuaciones a ecuaciones lineales
Res_Lineales = []
for Ec_x, Ec_y, Tipo, ValorEc in restricciones:
    if Tipo == '<=':
        ValorEc_lineal = ValorEc
    elif Tipo == '<':
        ValorEc_lineal = ValorEc
    elif Tipo == '>':
        ValorEc_lineal = ValorEc
    elif Tipo == '>=':
        ValorEc_lineal = ValorEc
    else: # Tipo == '='
        ValorEc_lineal = ValorEc
    Res_Lineales.append((Ec_x, Ec_y, '=', ValorEc_lineal))

# Definir el rango de valores para x y y
x_vals = np.linspace(0, 2000, 200)
y_vals = np.linspace(0, 2000, 200)

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Definir colores para las líneas
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] # Lista de colores para las líneas

ax.set_xlim(left=0, right=2000)
ax.set_ylim(bottom=0, top=2000)

# Para cada ecuación lineal, calcular y trazar la línea
for i, (Ec_x, Ec_y, Tipo, ValorEc) in enumerate(Res_Lineales):
    # Calcular los valores de y para cada valor de x
    y_line = (ValorEc - Ec_x * x_vals) / Ec_y
    # Trazar la línea con un color diferente
    ax.plot(x_vals, y_line, color=colors[i % len(colors)], label= restricciones[i])

# Configurar el gráfico
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Gráfico de las restricciones')
ax.legend() # Mostrar la leyenda

# Mostrar el gráfico
plt.show()