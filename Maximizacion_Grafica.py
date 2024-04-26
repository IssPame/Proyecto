# Librerias necesarias
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definicion de simbolos
x, y = sp.symbols('x, y')

# Funcion para validar el operador de la inecuacion
# Raise interrumpe el programa y activa el manejo de excepciones
def Operadores(op):
    Op_Validos = ['<=', '<', '>', '>=']
    if op not in Op_Validos:
        raise ValueError(f"Ingrese un operador valido {Op_Validos}")
    return op

# Solicitud de datos de la funcion objetivo
F_Obj_x = float(input("Indique el valor de X1 en la funcion objetivo: "))
F_Obj_y = float(input("Indique el valor de X2 en la funcion objetivo: "))
Z = F_Obj_x*x + F_Obj_y*y
print("La función objetivo es: Z = ", Z)
print()

# Solicitud de datos de las restricciones
Restricciones = int(input("Indique el numero de restricciones: "))
restricciones = []

for i in range(Restricciones):
    print()
    Ec_x = float(input(f"Indique el valor de X1 en la restriccion {i+1}: "))
    Ec_y = float(input(f"Indique el valor de X2 en la restriccion {i+1}: "))
    Tipo = input("Indique el tipo de restriccion (<=, <, >, >=): ")
    while Tipo not in ['<=', '<', '>', '>=']:
        print("Operador inválido. Intente de nuevo.")
        Tipo = input("Indique el tipo de restricción (<=, <, >, >=): ")
    Tipo = Operadores(Tipo)
    ValorEc = float(input(f"Indique el valor de la restriccion {i+1}: "))
    restricciones.append((Ec_x, Ec_y, Tipo, ValorEc))
print()

for i, (Ec_x, Ec_y, Tipo, ValorEc) in enumerate(restricciones, start=1):
    print(f"Restriccion {i}: {Ec_x}*x1 + {Ec_y}*x2 {Tipo} {ValorEc}")
print()

