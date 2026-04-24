from utils.simularUsuarios import simular_usuarios
from utils.simularProductos import simular_productos
from utils.simularEmpleados import simular_empleados
from notebook.limpieza import limpiarDatos, limpiar_productos, limpiar_empleados
import pandas as pd

# Mostrar todas las columnas sin truncar
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

usuarios = simular_usuarios(10)
productos = simular_productos(10)
empleados = simular_empleados(10)

simulaciones_usuarios = pd.DataFrame(usuarios)
simulaciones_productos = pd.DataFrame(productos)
simulaciones_empleados = pd.DataFrame(empleados)

limpios_usuarios = limpiarDatos(simulaciones_usuarios)
limpios_productos = limpiar_productos(simulaciones_productos)
limpios_empleados = limpiar_empleados(simulaciones_empleados)

print("Mostrando 10 registros limpios de usuarios")
print(limpios_usuarios)
print("\nMostrando 10 registros limpios de productos")
print(limpios_productos)
print("\nMostrando 10 registros limpios de empleados")
print(limpios_empleados)






##simulaciones_ordenadas.to_json("data/usuarios.json",orient="records",indent=4)
##
##simulaciones_ordenadas.to_csv("data/usuarios.csv")

